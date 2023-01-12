x <- read.csv("C:/Python_Workspace/03_Bigdata/03_Statistics_basic/3. Logistic Regression Analysis/churn.csv", header=TRUE)
y <- x[,19] # quality 열 추출

#hist(y)
#qqnorm(y)
#qqline(y, col=1)

#ks.test(y, "pnorm", mean = mean(y), sd = sd(y))

m <- glm(Churn ~ ., data = x)
summary(m)
m2 <- step(m, direction = 'both')
summary(m2)
#res = residuals(m2)
#qqnorm(res)
#qqline(res, col=1)
#ks.test(res, "pnorm", mean = mean(res), sd = sd(res))

#m3 <- glm(quality ~ ., family = 'poisson', data = x)
#summary(m3)
#m4 <- step(m3, direction = 'both')
#summary(m4)

#x.pca <- prcomp(x, center = T, scale. = T)
#print(x.pca)
#plot(x.pca, type='l')

