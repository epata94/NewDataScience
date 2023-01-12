churn_data <- read.csv("C:/Python_Workspace/04_bigdata/03_Statistics_basic/3_Logistic_Regression_Analysis/churn.csv", header=TRUE)

# head(churn_data, n=20)

# make a list of columns to be deleted
drops = c('State', 'Phone')

# column delete
churn_data <- churn_data[, !(names(churn_data) %in% drops)]

# Check the upper 20 rows of the dataframe after delete
head(churn_data, n=20)

# make basic statistics
summary(churn_data)

# check each variables' format
str(churn_data)

# make the logistic regression with the whole columns
churn_logit <- glm(Churn. ~., data = churn_data, family = 'binomial')
summary(churn_logit)

# execute variable choice by both direction
churn_logit_choice <- step(churn_logit, direction = 'both')
summary(churn_logit_choice)
