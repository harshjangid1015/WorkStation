

library(ISLR)
fix(USArrests)
summary(USArrests)
names(USArrests)
USArrests.labs=USArrests$labs
USArrests.data=USArrests$data
dim(USArrests)
usr.data=scale(USArrests)

library(ISLR)
dim(USArrests)
usr.dist=dist(USArrests)

plot(hclust(usr.dist), main=" Complete Linkage ", xlab ="", sub ="", ylab ="")
hc.out=hclust(usr.dist)
plot(hc.out)
hc.clusters=cutree(hc.out,3)
table(hc.clusters)
summary(hc.clusters)
plot(hc.out)
abline(h=150, col="red")
usr.labs=USArrests$labs
summary(usr.labs)
table(hc.clusters, labels(USArrests))
labels(USArrests)
usr.labs=labels(USArrests)
summary(usr.labs)
table(hc.clusters, usr.labs)
summary(hc.out)
table(hc.out)


sd.data=scale(usr.dist)
usr.dist=dist(sd.data)
hc.out=hclust(usr.dist)
plot(hc.out)
hc.clusters=cutree(hc.out,3)
abline(h=13, col="red")
table(hc.clusters)
