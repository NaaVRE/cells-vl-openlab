setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--var1"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--var2"), action="store", default=NA, type="integer", help="my description"),
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

print("Retrieving var1")
var = opt$var1
print(var)
var_len = length(var)
print(paste("Variable var1 has length", var_len))

var1 = opt$var1
print("Retrieving var2")
var = opt$var2
print(var)
var_len = length(var)
print(paste("Variable var2 has length", var_len))

var2 = opt$var2
id <- gsub('"', '', opt$id)


print("Running the cell")
var3 = var1+var2
