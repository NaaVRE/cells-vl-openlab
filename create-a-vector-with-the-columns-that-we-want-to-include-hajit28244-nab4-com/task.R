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

make_option(c("--data1"), action="store", default=NA, type="character", help="my description"),
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

print("Retrieving data1")
var = opt$data1
print(var)
var_len = length(var)
print(paste("Variable data1 has length", var_len))

print("------------------------Running var_serialization for data1-----------------------")
print(opt$data1)
data1 = var_serialization(opt$data1)
print("---------------------------------------------------------------------------------")

id <- gsub('"', '', opt$id)


print("Running the cell")
vector_column=c("scientificname", "adaptation", "stateprovince", "aquifer", "decimallatitude", "decimallongitude", "locationremarks")

mydataset = subset(data1, select = vector_column)

summary(mydataset)
# capturing outputs
print('Serialization of mydataset')
file <- file(paste0('/tmp/mydataset_', id, '.json'))
writeLines(toJSON(mydataset, auto_unbox=TRUE), file)
close(file)
