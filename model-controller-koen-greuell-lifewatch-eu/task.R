setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--my_input"), action="store", default=NA, type="character", help="my description"),
make_option(c("--my_other_input"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--param_something"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving my_input")
var = opt$my_input
print(var)
var_len = length(var)
print(paste("Variable my_input has length", var_len))

my_input <- gsub("\"", "", opt$my_input)
print("Retrieving my_other_input")
var = opt$my_other_input
print(var)
var_len = length(var)
print(paste("Variable my_other_input has length", var_len))

my_other_input = opt$my_other_input
print("Retrieving param_something")
var = opt$param_something
print(var)
var_len = length(var)
print(paste("Variable param_something has length", var_len))

param_something <- gsub("\"", "", opt$param_something)
id <- gsub('"', '', opt$id)


print("Running the cell")

# capturing outputs
print('Serialization of my_other_output')
file <- file(paste0('/tmp/my_other_output_', id, '.json'))
writeLines(toJSON(my_other_output, auto_unbox=TRUE), file)
close(file)
print('Serialization of my_output')
file <- file(paste0('/tmp/my_output_', id, '.json'))
writeLines(toJSON(my_output, auto_unbox=TRUE), file)
close(file)
