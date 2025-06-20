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

id <- gsub('"', '', opt$id)


print("Running the cell")
data1=read.csv("/home/jovyan/naa-vre-public/sara_and_ale/Dataset.csv", sep=",")
summary(data1)
# capturing outputs
print('Serialization of data1')
file <- file(paste0('/tmp/data1_', id, '.json'))
writeLines(toJSON(data1, auto_unbox=TRUE), file)
close(file)
