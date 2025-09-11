setwd('/app')
library(optparse)
library(jsonlite)

if (!requireNamespace("tidyverse", quietly = TRUE)) {
	install.packages("tidyverse", repos="http://cran.us.r-project.org")
}
library(tidyverse)
if (!requireNamespace("terra", quietly = TRUE)) {
	install.packages("terra", repos="http://cran.us.r-project.org")
}
library(terra)



print('option_list')
option_list = list(

make_option(c("--BCEF"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--Coniferous_ratio"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--Deadwood_lying_m3/ha"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--Deadwood_standing_m3/ha"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--Growingstock_m3/ha"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--Liter_stock_kg.c/ha"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--LU_1970"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--LU_1990"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--LU_2004"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--LU_2009"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--LU_2013"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--LU_2017"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--LU_2021"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--param_above_ground_biomass"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--Rootshoot_ratio"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--Soil_1970"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--Soil_2012"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--id"), action="store", default=NA, type="character", help="task id")
)


opt = parse_args(OptionParser(option_list=option_list))

var_serialization <- function(var){
    if (is.null(var)){
        print("Variable is null")
        exit(1)
    }
    tryCatch(
        {
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        },
        error=function(e) {
            print("Error while deserializing the variable")
            print(var)
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        },
        warning=function(w) {
            print("Warning while deserializing the variable")
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        }
    )
}

print("Retrieving BCEF")
var = opt$BCEF
print(var)
var_len = length(var)
print(paste("Variable BCEF has length", var_len))

BCEF = opt$BCEF
print("Retrieving Coniferous_ratio")
var = opt$Coniferous_ratio
print(var)
var_len = length(var)
print(paste("Variable Coniferous_ratio has length", var_len))

Coniferous_ratio = opt$Coniferous_ratio
print("Retrieving Deadwood_lying_m3/ha")
var = opt$Deadwood_lying_m3/ha
print(var)
var_len = length(var)
print(paste("Variable Deadwood_lying_m3/ha has length", var_len))

Deadwood_lying_m3/ha = opt$Deadwood_lying_m3/ha
print("Retrieving Deadwood_standing_m3/ha")
var = opt$Deadwood_standing_m3/ha
print(var)
var_len = length(var)
print(paste("Variable Deadwood_standing_m3/ha has length", var_len))

Deadwood_standing_m3/ha = opt$Deadwood_standing_m3/ha
print("Retrieving Growingstock_m3/ha")
var = opt$Growingstock_m3/ha
print(var)
var_len = length(var)
print(paste("Variable Growingstock_m3/ha has length", var_len))

Growingstock_m3/ha = opt$Growingstock_m3/ha
print("Retrieving Liter_stock_kg.c/ha")
var = opt$Liter_stock_kg.c/ha
print(var)
var_len = length(var)
print(paste("Variable Liter_stock_kg.c/ha has length", var_len))

Liter_stock_kg.c/ha = opt$Liter_stock_kg.c/ha
print("Retrieving LU_1970")
var = opt$LU_1970
print(var)
var_len = length(var)
print(paste("Variable LU_1970 has length", var_len))

LU_1970 = opt$LU_1970
print("Retrieving LU_1990")
var = opt$LU_1990
print(var)
var_len = length(var)
print(paste("Variable LU_1990 has length", var_len))

LU_1990 = opt$LU_1990
print("Retrieving LU_2004")
var = opt$LU_2004
print(var)
var_len = length(var)
print(paste("Variable LU_2004 has length", var_len))

LU_2004 = opt$LU_2004
print("Retrieving LU_2009")
var = opt$LU_2009
print(var)
var_len = length(var)
print(paste("Variable LU_2009 has length", var_len))

LU_2009 = opt$LU_2009
print("Retrieving LU_2013")
var = opt$LU_2013
print(var)
var_len = length(var)
print(paste("Variable LU_2013 has length", var_len))

LU_2013 = opt$LU_2013
print("Retrieving LU_2017")
var = opt$LU_2017
print(var)
var_len = length(var)
print(paste("Variable LU_2017 has length", var_len))

LU_2017 = opt$LU_2017
print("Retrieving LU_2021")
var = opt$LU_2021
print(var)
var_len = length(var)
print(paste("Variable LU_2021 has length", var_len))

LU_2021 = opt$LU_2021
print("Retrieving param_above_ground_biomass")
var = opt$param_above_ground_biomass
print(var)
var_len = length(var)
print(paste("Variable param_above_ground_biomass has length", var_len))

param_above_ground_biomass = opt$param_above_ground_biomass
print("Retrieving Rootshoot_ratio")
var = opt$Rootshoot_ratio
print(var)
var_len = length(var)
print(paste("Variable Rootshoot_ratio has length", var_len))

Rootshoot_ratio = opt$Rootshoot_ratio
print("Retrieving Soil_1970")
var = opt$Soil_1970
print(var)
var_len = length(var)
print(paste("Variable Soil_1970 has length", var_len))

Soil_1970 = opt$Soil_1970
print("Retrieving Soil_2012")
var = opt$Soil_2012
print(var)
var_len = length(var)
print(paste("Variable Soil_2012 has length", var_len))

Soil_2012 = opt$Soil_2012
id <- gsub('"', '', opt$id)


print("Running the cell")

# capturing outputs
print('Serialization of ER_output')
file <- file(paste0('/tmp/ER_output_', id, '.json'))
writeLines(toJSON(ER_output, auto_unbox=TRUE), file)
close(file)
