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
url <- "https://zenodo.org/records/14793316/files/Dataset.csv?download=1"
data1_path <- "/tmp/data/Dataset.csv"  # This will save the file in your working directory

download.file(url, data1_path, mode = "wb")
# capturing outputs
print('Serialization of data1_path')
file <- file(paste0('/tmp/data1_path_', id, '.json'))
writeLines(toJSON(data1_path, auto_unbox=TRUE), file)
close(file)
