setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--fair_data_1"), action="store", default=NA, type="character", help="my description"),
make_option(c("--fair_data_2"), action="store", default=NA, type="character", help="my description"),
make_option(c("--fair_data_3"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving fair_data_1")
var = opt$fair_data_1
print(var)
var_len = length(var)
print(paste("Variable fair_data_1 has length", var_len))

fair_data_1 <- gsub("\"", "", opt$fair_data_1)
print("Retrieving fair_data_2")
var = opt$fair_data_2
print(var)
var_len = length(var)
print(paste("Variable fair_data_2 has length", var_len))

fair_data_2 <- gsub("\"", "", opt$fair_data_2)
print("Retrieving fair_data_3")
var = opt$fair_data_3
print(var)
var_len = length(var)
print(paste("Variable fair_data_3 has length", var_len))

fair_data_3 <- gsub("\"", "", opt$fair_data_3)
id <- gsub('"', '', opt$id)


print("Running the cell")
print(fair_data_1)
print(fair_data_2)
print(fair_data_3)


input_data <- "combined_data"
# capturing outputs
print('Serialization of input_data')
file <- file(paste0('/tmp/input_data_', id, '.json'))
writeLines(toJSON(input_data, auto_unbox=TRUE), file)
close(file)
