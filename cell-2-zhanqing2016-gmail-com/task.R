setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--output1"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--output2"), action="store", default=NA, type="integer", help="my description"),
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

print("Retrieving output1")
var = opt$output1
print(var)
var_len = length(var)
print(paste("Variable output1 has length", var_len))

output1 = opt$output1
print("Retrieving output2")
var = opt$output2
print(var)
var_len = length(var)
print(paste("Variable output2 has length", var_len))

output2 = opt$output2
id <- gsub('"', '', opt$id)


print("Running the cell")
var1 = output1
var2 = output2
# capturing outputs
print('Serialization of var1')
file <- file(paste0('/tmp/var1_', id, '.json'))
writeLines(toJSON(var1, auto_unbox=TRUE), file)
close(file)
print('Serialization of var2')
file <- file(paste0('/tmp/var2_', id, '.json'))
writeLines(toJSON(var2, auto_unbox=TRUE), file)
close(file)
