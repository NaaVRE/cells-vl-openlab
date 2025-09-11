setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--model_parameters"), action="store", default=NA, type="character", help="my description"),
make_option(c("--preprocessed_data"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving model_parameters")
var = opt$model_parameters
print(var)
var_len = length(var)
print(paste("Variable model_parameters has length", var_len))

print("------------------------Running var_serialization for model_parameters-----------------------")
print(opt$model_parameters)
model_parameters = var_serialization(opt$model_parameters)
print("---------------------------------------------------------------------------------")

print("Retrieving preprocessed_data")
var = opt$preprocessed_data
print(var)
var_len = length(var)
print(paste("Variable preprocessed_data has length", var_len))

print("------------------------Running var_serialization for preprocessed_data-----------------------")
print(opt$preprocessed_data)
preprocessed_data = var_serialization(opt$preprocessed_data)
print("---------------------------------------------------------------------------------")

id <- gsub('"', '', opt$id)


print("Running the cell")
model_results <- list()
model_results <- preprocessed_data
print(model_parameters)
# capturing outputs
print('Serialization of model_results')
file <- file(paste0('/tmp/model_results_', id, '.json'))
writeLines(toJSON(model_results, auto_unbox=TRUE), file)
close(file)
