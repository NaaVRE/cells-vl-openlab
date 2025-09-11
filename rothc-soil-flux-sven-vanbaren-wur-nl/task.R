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
print('Serialization of Cropland_flux_co2/ha')
file <- file(paste0('/tmp/Cropland_flux_co2/ha_', id, '.json'))
writeLines(toJSON(Cropland_flux_co2/ha, auto_unbox=TRUE), file)
close(file)
print('Serialization of Grassland_flux_co2/ha')
file <- file(paste0('/tmp/Grassland_flux_co2/ha_', id, '.json'))
writeLines(toJSON(Grassland_flux_co2/ha, auto_unbox=TRUE), file)
close(file)
