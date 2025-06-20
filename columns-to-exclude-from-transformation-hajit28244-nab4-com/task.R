setwd('/app')
library(optparse)
library(jsonlite)

if (!requireNamespace("cowplot", quietly = TRUE)) {
	install.packages("cowplot", repos="http://cran.us.r-project.org")
}
library(cowplot)
if (!requireNamespace("ggplot2", quietly = TRUE)) {
	install.packages("ggplot2", repos="http://cran.us.r-project.org")
}
library(ggplot2)
if (!requireNamespace("ggspatial", quietly = TRUE)) {
	install.packages("ggspatial", repos="http://cran.us.r-project.org")
}
library(ggspatial)
if (!requireNamespace("sf", quietly = TRUE)) {
	install.packages("sf", repos="http://cran.us.r-project.org")
}
library(sf)



print('option_list')
option_list = list(

make_option(c("--as.factor"), action="store", default=NA, type="character", help="my description"),
make_option(c("--mydataset"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving as.factor")
var = opt$as.factor
print(var)
var_len = length(var)
print(paste("Variable as.factor has length", var_len))

print("------------------------Running var_serialization for as.factor-----------------------")
print(opt$as.factor)
as.factor = var_serialization(opt$as.factor)
print("---------------------------------------------------------------------------------")

print("Retrieving mydataset")
var = opt$mydataset
print(var)
var_len = length(var)
print(paste("Variable mydataset has length", var_len))

print("------------------------Running var_serialization for mydataset-----------------------")
print(opt$mydataset)
mydataset = var_serialization(opt$mydataset)
print("---------------------------------------------------------------------------------")

id <- gsub('"', '', opt$id)


print("Running the cell")
exclude_cols = c("decimallatitude", "decimallongitude")

mydataset[ , !(names(mydataset) %in% exclude_cols)] = 
  lapply(mydataset[ , !(names(mydataset) %in% exclude_cols)], as.factor)

summary(mydataset)
