setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--param_setting1"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving param_setting1")
var = opt$param_setting1
print(var)
var_len = length(var)
print(paste("Variable param_setting1 has length", var_len))

param_setting1 <- gsub("\"", "", opt$param_setting1)
id <- gsub('"', '', opt$id)


print("Running the cell")
model_parameters <- list(param_setting1)
# capturing outputs
print('Serialization of model_parameters')
file <- file(paste0('/tmp/model_parameters_', id, '.json'))
writeLines(toJSON(model_parameters, auto_unbox=TRUE), file)
close(file)
