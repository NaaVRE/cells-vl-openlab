setwd('/app')
library(optparse)
library(jsonlite)

if (!requireNamespace("getRad", quietly = TRUE)) {
	install.packages("getRad", repos="http://cran.us.r-project.org")
}
library(getRad)



print('option_list')
option_list = list(

make_option(c("--country"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving country")
var = opt$country
print(var)
var_len = length(var)
print(paste("Variable country has length", var_len))

country <- gsub("\"", "", opt$country)
id <- gsub('"', '', opt$id)


print("Running the cell")
library(getRad)

print(country)
print("getRad has version:")
print(packageVersion("getRad"))
