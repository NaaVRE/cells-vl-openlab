setwd('/app')
library(optparse)
library(jsonlite)

if (!requireNamespace("aws.s3", quietly = TRUE)) {
	install.packages("aws.s3", repos="http://cran.us.r-project.org")
}
library(aws.s3)



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

{'name': 'conf_data_path', 'assignation': 'conf_data_path="/tmp/data"'}

print("Running the cell")
library("aws.s3")
Sys.setenv("AWS_S3_ENDPOINT" = param_minio_endpoint,
           "AWS_DEFAULT_REGION" = param_minio_region,
           "AWS_ACCESS_KEY_ID" = secret_minio_access_key,
           "AWS_SECRET_ACCESS_KEY" = secret_minio_secret_key)

bucketlist()



file=paste0(conf_data_path,"/ant_coordinates.csv")
save_object(bucket="naa-vre-user-data", object=paste0(param_minio_user_prefix, "/datafile/ant_coordinates.csv"), file=file)
# capturing outputs
print('Serialization of file')
file <- file(paste0('/tmp/file_', id, '.json'))
writeLines(toJSON(file, auto_unbox=TRUE), file)
close(file)
