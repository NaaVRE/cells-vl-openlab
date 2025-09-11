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
print('Serialization of LU_1970')
file <- file(paste0('/tmp/LU_1970_', id, '.json'))
writeLines(toJSON(LU_1970, auto_unbox=TRUE), file)
close(file)
print('Serialization of LU_1990')
file <- file(paste0('/tmp/LU_1990_', id, '.json'))
writeLines(toJSON(LU_1990, auto_unbox=TRUE), file)
close(file)
print('Serialization of LU_2004')
file <- file(paste0('/tmp/LU_2004_', id, '.json'))
writeLines(toJSON(LU_2004, auto_unbox=TRUE), file)
close(file)
print('Serialization of LU_2009')
file <- file(paste0('/tmp/LU_2009_', id, '.json'))
writeLines(toJSON(LU_2009, auto_unbox=TRUE), file)
close(file)
print('Serialization of LU_2013')
file <- file(paste0('/tmp/LU_2013_', id, '.json'))
writeLines(toJSON(LU_2013, auto_unbox=TRUE), file)
close(file)
print('Serialization of LU_2017')
file <- file(paste0('/tmp/LU_2017_', id, '.json'))
writeLines(toJSON(LU_2017, auto_unbox=TRUE), file)
close(file)
print('Serialization of LU_2021')
file <- file(paste0('/tmp/LU_2021_', id, '.json'))
writeLines(toJSON(LU_2021, auto_unbox=TRUE), file)
close(file)
