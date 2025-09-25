setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--dataset_1"), action="store", default=NA, type="character", help="my description"),
make_option(c("--dataset_2"), action="store", default=NA, type="character", help="my description"),
make_option(c("--dataset_3"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving dataset_1")
var = opt$dataset_1
print(var)
var_len = length(var)
print(paste("Variable dataset_1 has length", var_len))

dataset_1 <- gsub("\"", "", opt$dataset_1)
print("Retrieving dataset_2")
var = opt$dataset_2
print(var)
var_len = length(var)
print(paste("Variable dataset_2 has length", var_len))

dataset_2 <- gsub("\"", "", opt$dataset_2)
print("Retrieving dataset_3")
var = opt$dataset_3
print(var)
var_len = length(var)
print(paste("Variable dataset_3 has length", var_len))

dataset_3 <- gsub("\"", "", opt$dataset_3)
id <- gsub('"', '', opt$id)


print("Running the cell")
print(dataset_1)
print(dataset_2)
print(dataset_3)

fair_data_1 <- "fair_data_1"
fair_data_2 <- "fair_data_2"
fair_data_3 <- "fair_data_3"
# capturing outputs
print('Serialization of fair_data_1')
file <- file(paste0('/tmp/fair_data_1_', id, '.json'))
writeLines(toJSON(fair_data_1, auto_unbox=TRUE), file)
close(file)
print('Serialization of fair_data_2')
file <- file(paste0('/tmp/fair_data_2_', id, '.json'))
writeLines(toJSON(fair_data_2, auto_unbox=TRUE), file)
close(file)
print('Serialization of fair_data_3')
file <- file(paste0('/tmp/fair_data_3_', id, '.json'))
writeLines(toJSON(fair_data_3, auto_unbox=TRUE), file)
close(file)
