setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--var1"), action="store", default=NA, type="integer", help="my description"),
make_option(c("--var3"), action="store", default=NA, type="integer", help="my description"),
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
print("Retrieving var3")
var = opt$var3
print(var)
var_len = length(var)
print(paste("Variable var3 has length", var_len))

var3 = opt$var3
id <- gsub('"', '', opt$id)


print("Running the cell")
var2 <- var1
var4 <- var3
# capturing outputs
print('Serialization of var2')
file <- file(paste0('/tmp/var2_', id, '.json'))
writeLines(toJSON(var2, auto_unbox=TRUE), file)
close(file)
print('Serialization of var4')
file <- file(paste0('/tmp/var4_', id, '.json'))
writeLines(toJSON(var4, auto_unbox=TRUE), file)
close(file)
