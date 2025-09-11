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
print('Serialization of Cropland_mineralsoil_ton.c/ha')
file <- file(paste0('/tmp/Cropland_mineralsoil_ton.c/ha_', id, '.json'))
writeLines(toJSON(Cropland_mineralsoil_ton.c/ha, auto_unbox=TRUE), file)
close(file)
print('Serialization of Forestland_mineralsoil_ton.c/ha')
file <- file(paste0('/tmp/Forestland_mineralsoil_ton.c/ha_', id, '.json'))
writeLines(toJSON(Forestland_mineralsoil_ton.c/ha, auto_unbox=TRUE), file)
close(file)
print('Serialization of Grassland_mineralsoil_ton.c/ha')
file <- file(paste0('/tmp/Grassland_mineralsoil_ton.c/ha_', id, '.json'))
writeLines(toJSON(Grassland_mineralsoil_ton.c/ha, auto_unbox=TRUE), file)
close(file)
print('Serialization of Settlements_mineralsoil_ton.c/ha')
file <- file(paste0('/tmp/Settlements_mineralsoil_ton.c/ha_', id, '.json'))
writeLines(toJSON(Settlements_mineralsoil_ton.c/ha, auto_unbox=TRUE), file)
close(file)
print('Serialization of Trees outside forest_mineralsoil_ton.c/ha')
file <- file(paste0('/tmp/Trees outside forest_mineralsoil_ton.c/ha_', id, '.json'))
writeLines(toJSON(Trees outside forest_mineralsoil_ton.c/ha, auto_unbox=TRUE), file)
close(file)
print('Serialization of Wetlands_mineralsoil_ton.c/ha')
file <- file(paste0('/tmp/Wetlands_mineralsoil_ton.c/ha_', id, '.json'))
writeLines(toJSON(Wetlands_mineralsoil_ton.c/ha, auto_unbox=TRUE), file)
close(file)
