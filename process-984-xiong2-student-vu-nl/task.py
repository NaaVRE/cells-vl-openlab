import time
import numpy as np

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--work_items', action='store', type=str, required=True, dest='work_items')


args = arg_parser.parse_args()
print(args)

id = args.id

work_items = json.loads(args.work_items)



MAT_N = 800        # 方阵大小（GEMM/Cholesky/SVD 的主耗时来源）
FFT_N = 32768      # FFT 点数
TOPK  = 16         # 取前几大奇异值
REPEAT = 5         # 每个元素重复执行重计算的次数，用来放大单任务时长




def run_serial_heavy(work_items, MAT_N, FFT_N, TOPK=16, REPEAT=1):
    """
    单函数：外层只对 work_items 迭代（数量可小到 4）。
    为了让“每个元素”足够重，内部使用 REPEAT 次高代价运算：
      - GEMM/Cholesky/解线性方程
      - 子块 SVD
      - 大规模 rFFT 能量聚合
      - 额外非线性标量统计
    这样即便只有 4 个输入元素，也能显著占用计算资源，利于容器化并行按元素分片。
    """
    t0 = time.perf_counter()
    acc = 0.0

    for i in work_items:                 # ← 可直接按元素分片并行
        rng = np.random.default_rng(i)

        for _ in range(REPEAT):          # 放大单元素的计算时长
            A = rng.standard_normal((MAT_N, MAT_N), dtype=np.float64)
            M = A.T @ A + np.eye(MAT_N, dtype=np.float64) * 1e-3   # GEMM + 正则项
            L = np.linalg.cholesky(M)

            b = rng.standard_normal(MAT_N, dtype=np.float64)
            y = np.linalg.solve(L, b)
            x = np.linalg.solve(L.T, y)
            acc += float(x[:16] @ x[:16])

            B = A[:256, :256]
            U, S, Vt = np.linalg.svd(B, full_matrices=False)
            acc += float(S[:min(TOPK, S.size)].sum())

            sig = rng.standard_normal(FFT_N, dtype=np.float64)
            spec = np.fft.rfft(sig)
            acc += float(np.vdot(spec, spec).real)

            z = np.tanh(B).mean() + np.cos(B).std()
            acc += float(z)

            del A, M, L, b, y, x, B, U, S, Vt, sig, spec

    elapsed = time.perf_counter() - t0
    print(f"Aggregate = {acc:.6e}")
    print(f"总运行时间: {elapsed:.3f} 秒  (|work_items|={len(work_items)}, MAT_N={MAT_N}, FFT_N={FFT_N}, TOPK={TOPK}, REPEAT={REPEAT})")
    return acc, elapsed

run_serial_heavy(work_items, MAT_N, FFT_N, TOPK, REPEAT)

