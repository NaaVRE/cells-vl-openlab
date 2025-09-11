setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--model"), action="store", default=NA, type="character", help="my description"),
make_option(c("--x"), action="store", default=NA, type="numeric", help="my description"),
make_option(c("--y"), action="store", default=NA, type="numeric", help="my description"),
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

print("Retrieving model")
var = opt$model
print(var)
var_len = length(var)
print(paste("Variable model has length", var_len))

print("------------------------Running var_serialization for model-----------------------")
print(opt$model)
model = var_serialization(opt$model)
print("---------------------------------------------------------------------------------")

print("Retrieving x")
var = opt$x
print(var)
var_len = length(var)
print(paste("Variable x has length", var_len))

x = opt$x
print("Retrieving y")
var = opt$y
print(var)
var_len = length(var)
print(paste("Variable y has length", var_len))

y = opt$y
id <- gsub('"', '', opt$id)


print("Running the cell")
x_pred <- data.frame(x = seq(-3,3, 0.5))
y_pred <- predict(model, newdata = x_pred)
str(y_pred)
plot(x_pred$x, y_pred)
