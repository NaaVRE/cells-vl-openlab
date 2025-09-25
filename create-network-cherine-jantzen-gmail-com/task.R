setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--input_data"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving input_data")
var = opt$input_data
print(var)
var_len = length(var)
print(paste("Variable input_data has length", var_len))

input_data <- gsub("\"", "", opt$input_data)
id <- gsub('"', '', opt$id)


print("Running the cell")
print(input_data)

network_structure <- "network_structure"
# capturing outputs
print('Serialization of network_structure')
file <- file(paste0('/tmp/network_structure_', id, '.json'))
writeLines(toJSON(network_structure, auto_unbox=TRUE), file)
close(file)
