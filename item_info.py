# -*- coding: utf-8 -*-
from google.appengine.ext import db

class items(db.Expando):
	company=db.StringProperty(multiline=True) #品牌名稱(utf-8)
	category=db.StringProperty(multiline=True) #商品類別(utf-8)
	url=db.StringProperty(multiline=True) #檔案櫃網址(圖檔)
	series=db.StringProperty(multiline=True) #商品型號
	inventory=db.IntegerProperty()#庫存量
	pic=db.StringProperty(multiline=True)#圖檔名稱(utf-8)
	item=db.StringProperty(multiline=True)#商品名稱(utf-8)
	price=db.IntegerProperty()#價格
a=db.GqlQuery("select * from items order by company DESC")
for i in a.run():
	print "<html><meta http-equiv='Content-Type' content='text/html;charset=utf-8'><body>"
	print "<p>品牌名稱：%s<br>"%(i.company.encode('utf-8'))
	print "商品類別：%s<br>"%(i.category.encode('utf-8'))
	print "圖檔名稱：%s<br>"%(i.pic.encode('utf-8'))
	print "商品型號：%s<br>"%(i.series.encode('utf-8'))
	print "<a href=%s/%s target='_blank'><img src=%s/%s height=50></a></p>"%(i.url,i.pic.encode('utf-8'),i.url,i.pic.encode('utf-8'))
print "</body></html>"