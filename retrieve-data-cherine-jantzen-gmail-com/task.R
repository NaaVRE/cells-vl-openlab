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
dataset_1 <- "dataset_1"
dataset_2 <- "dataset_2"
dataset_3 <- "dataset_3"
# capturing outputs
print('Serialization of dataset_1')
file <- file(paste0('/tmp/dataset_1_', id, '.json'))
writeLines(toJSON(dataset_1, auto_unbox=TRUE), file)
close(file)
print('Serialization of dataset_2')
file <- file(paste0('/tmp/dataset_2_', id, '.json'))
writeLines(toJSON(dataset_2, auto_unbox=TRUE), file)
close(file)
print('Serialization of dataset_3')
file <- file(paste0('/tmp/dataset_3_', id, '.json'))
writeLines(toJSON(dataset_3, auto_unbox=TRUE), file)
close(file)
