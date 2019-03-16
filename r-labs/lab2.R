# import libraries
library(MASS)

# print initial data set
head(mtcars)

# Main components method
#==================================================
# perform a principal components analysis on the
PCA <- princomp(scale(mtcars))
summary(PCA)

plot(cumsum(PCA$sdev) / sum(PCA$sdev), ylab = "Proportion of explained variance")

plot(PCA)
biplot(PCA)

# visualise some components variance
plot(PCA$scores, col=factor(mtcars$cyl), main="cylinders count (cyl)")
plot(PCA$scores, col=factor(mtcars$carb), main="car brand (carb)")
plot(PCA$scores, col=factor(mtcars$am), main="transmission (0 = automatic, 1 = manual) (am)")

# LDA
#==================================================
lda(cyl ~., data=mtcars)

plot(lda(cyl ~., data=mtcars), main="cylinders (cyl)")
plot(lda(gear ~., data=mtcars), main="number of forward gears (gear)")

plot(lda(carb ~., data=mtcars), main="car brand (carb)")
plot(lda(am ~., data=mtcars), main="transmission")

# Factor analysis
#==================================================


