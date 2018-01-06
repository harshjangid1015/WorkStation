set.seed(1)
x1=runif(500)-0.5
set.seed(2)
x2=runif(500)-0.5
y=1*(x1^2-x2^2 > 0)
plot(x1, x2, col=(y+1))
glm.fit=glm(y~x1+x2, family = binomial)
glm.prob=predict(glm.fit, type = "response")
glm.prob[1:10]
contrasts()
rm(glm.pred)
plot(glm.prob, y, col=y+1)

glm.pred=rep("Down",500)
glm.pred[glm.prob>0.5]="up"
glm.pred[1:10]
table(glm.pred)

glm.fit=glm(y~x1+x2+x1^2, family = binomial)
glm.prob=predict(glm.fit, type = "response")
plot(glm.prob, y, col=y+1)
table(glm.prob)
