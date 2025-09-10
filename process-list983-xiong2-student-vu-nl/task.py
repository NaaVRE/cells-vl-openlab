import time
import math

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



J = 500                       
K = 500
def run_serial(work_items, J, K):
    """单函数：内部包含计算核和三重循环"""
    start = time.perf_counter()
    result = 0.0

    for i in work_items:
        for j in range(J):
            for k in range(K):
                x = i * 1e-3 + j * 1e-4 + k * 1e-5

                s = math.sin(x) * math.cos(x + 0.3) + math.tanh(x - 0.2)
                t = math.log1p(abs(s)) + math.sqrt(abs(s) + 1e-9)

                a00, a01, a02 = (1.0 + x), (0.3 - s), (0.2 + t)
                a10, a11, a12 = (0.1 + s), (1.0 - x), (0.4 - t)
                a20, a21, a22 = (0.2 - t), (0.5 + x), (1.0 + s)
                v0, v1, v2 = x, s, t

                y0 = a00*v0 + a01*v1 + a02*v2
                y1 = a10*v0 + a11*v1 + a12*v2
                y2 = a20*v0 + a21*v1 + a22*v2

                z = y0*y0 + y1*y1 + y2*y2 + 1e-9
                inv = 1.0 / math.sqrt(z)
                for _ in range(3):
                    inv = inv * (1.5 - 0.5 * z * inv * inv)

                result += (y0 + 2.0*y1 + 3.0*y2) * inv * 1e-6

    elapsed = time.perf_counter() - start
    print(f"Result = {result}")
    print(f"总运行时间: {elapsed:.3f} 秒  (J={J}, K={K}, |work_items|={len(work_items)})")
    return result, elapsed

run_serial(work_items, J, K)

