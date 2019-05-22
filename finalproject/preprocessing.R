dealtype<- read.csv("/Users/leetsaiying/Desktop/17life/deal_type.csv")
class(dealtype)
order<-read.csv('/Users/leetsaiying/Desktop/17life/order.csv')
deal<-read.csv('/Users/leetsaiying/Desktop/17life/deal_change.csv',header=F)
deal2<-read.csv('/Users/leetsaiying/Desktop/17life/deal_change2.csv')
colnames(deal)<-c("business_hour_guid","item_origin","item_price","item_defa","deal_type","code_name","code","category")
deal<-deal[-1,]
test<-merge(x = order, y = deal, by = "business_hour_guid")
testout<-merge(x=order,y=deal,by="business_hour_guid",all=TRUE)
deal3<-read.csv('/Users/leetsaiying/Desktop/17life/deal.csv',header=F)
library(dplyr)
inner_join(order,deal)
#將user_id顯示在最前頭 創成testout_new
#mer<-testout[9]
#mer2<-testout[,-9]
#rm(testout)
testout_new<-cbind(mer,mer2)

totalbyid<-tapply(testout_new$subtotal,testout_new$user_id,sum)
#作出以同id算出的總花費
totalbyid<-aggregate(testout_new$subtotal,by=list(id=testout_new$user_id),FUN=sum)
#將欄位名稱改名
colnames(totalbyid)<-c("user_id","totalspend")

#利用testout_new這個表選取自己要的欄位創造table這個新表(user_id,business_hour_guid,subtotal,create_time,deal_type)
table<-testout_new[,c(1,2,6,8,15)]
rm(table)
