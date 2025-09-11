setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

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

id <- gsub('"', '', opt$id)


print("Running the cell")

# capturing outputs
print('Serialization of BCEF')
file <- file(paste0('/tmp/BCEF_', id, '.json'))
writeLines(toJSON(BCEF, auto_unbox=TRUE), file)
close(file)
print('Serialization of Coniferous_ratio')
file <- file(paste0('/tmp/Coniferous_ratio_', id, '.json'))
writeLines(toJSON(Coniferous_ratio, auto_unbox=TRUE), file)
close(file)
print('Serialization of Deadwood_lying_m3/ha')
file <- file(paste0('/tmp/Deadwood_lying_m3/ha_', id, '.json'))
writeLines(toJSON(Deadwood_lying_m3/ha, auto_unbox=TRUE), file)
close(file)
print('Serialization of Deadwood_standing_m3/ha')
file <- file(paste0('/tmp/Deadwood_standing_m3/ha_', id, '.json'))
writeLines(toJSON(Deadwood_standing_m3/ha, auto_unbox=TRUE), file)
close(file)
print('Serialization of Growingstock_m3/ha')
file <- file(paste0('/tmp/Growingstock_m3/ha_', id, '.json'))
writeLines(toJSON(Growingstock_m3/ha, auto_unbox=TRUE), file)
close(file)
print('Serialization of Liter_stock_kg.c/ha')
file <- file(paste0('/tmp/Liter_stock_kg.c/ha_', id, '.json'))
writeLines(toJSON(Liter_stock_kg.c/ha, auto_unbox=TRUE), file)
close(file)
print('Serialization of Rootshoot_ratio')
file <- file(paste0('/tmp/Rootshoot_ratio_', id, '.json'))
writeLines(toJSON(Rootshoot_ratio, auto_unbox=TRUE), file)
close(file)
