setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--model_results"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving model_results")
var = opt$model_results
print(var)
var_len = length(var)
print(paste("Variable model_results has length", var_len))

print("------------------------Running var_serialization for model_results-----------------------")
print(opt$model_results)
model_results = var_serialization(opt$model_results)
print("---------------------------------------------------------------------------------")

id <- gsub('"', '', opt$id)


print("Running the cell")
print(model_results)
