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
print('Serialization of Cropland')
file <- file(paste0('/tmp/Cropland_', id, '.json'))
writeLines(toJSON(Cropland, auto_unbox=TRUE), file)
close(file)
print('Serialization of Forestland')
file <- file(paste0('/tmp/Forestland_', id, '.json'))
writeLines(toJSON(Forestland, auto_unbox=TRUE), file)
close(file)
print('Serialization of Grassland')
file <- file(paste0('/tmp/Grassland_', id, '.json'))
writeLines(toJSON(Grassland, auto_unbox=TRUE), file)
close(file)
print('Serialization of Settlements')
file <- file(paste0('/tmp/Settlements_', id, '.json'))
writeLines(toJSON(Settlements, auto_unbox=TRUE), file)
close(file)
print('Serialization of Trees outside forest')
file <- file(paste0('/tmp/Trees outside forest_', id, '.json'))
writeLines(toJSON(Trees outside forest, auto_unbox=TRUE), file)
close(file)
print('Serialization of Wetlands')
file <- file(paste0('/tmp/Wetlands_', id, '.json'))
writeLines(toJSON(Wetlands, auto_unbox=TRUE), file)
close(file)
