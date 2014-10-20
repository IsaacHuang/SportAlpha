# -*- coding: utf-8 -*-
from google.appengine.ext import db
import cgi
form=cgi.FieldStorage()
brand=form.getvalue('brand','')#品牌名稱
series=form.getvalue('series','')#商品型號
Site=form.getvalue('Site','')#檔案櫃網址
pic=form.getvalue('pic','')#圖檔名稱
category=form.getvalue('category','')#商品類別
web_url=form.getvalue('web_url','')#品牌官網網址
inventory=form.getvalue('inventory','')#進貨數目
price=form.getvalue('price','')#價格
item=form.getvalue('item','')#商品名稱
url=form.getvalue('url','')#商品網址
class items(db.Expando):
	company=db.StringProperty(multiline=True) #品牌名稱(utf-8)
	category=db.StringProperty(multiline=True) #商品類別(utf-8)
	Site=db.StringProperty(multiline=True) #檔案櫃網址(圖檔)
	series=db.StringProperty(multiline=True) #商品型號('utf-8')
	inventory=db.IntegerProperty()#庫存量
	pic=db.StringProperty(multiline=True)#圖檔名稱(utf-8)
	Web_url=db.StringProperty(multiline=True)#官網網址(utf-8)
	price=db.IntegerProperty()#價位
	url=db.StringProperty(multiline=True)#商品網址
	item=db.StringProperty(multiline=True)#商品名稱('utf-8')
a=db.GqlQuery("select * from items order by company DESC")
judge=""
for i in a.run():
	if brand==i.company.encode('utf-8'):
		print "此廠商已存在！"
		judge="此廠商已存在！"
		print "<a href='/item_info'>回首頁</a>"
		print "<a href='/admin/item_info.html'>繼續新增資料</a>"
		break
if judge!="此廠商已存在！":
	inventory=int(inventory)
	price=int(price)
	goods=items(company=unicode(brand,'utf-8'),series=unicode(series,'utf-8'),Site=Site,pic=unicode(pic,'utf-8'),category=unicode(category,'utf-8'),inventory=inventory,Web_url=unicode(web_url,'utf-8'),price=price,url=url,item=unicode(item,'utf-8'))
	goods.put()
	print "資料已新增！"
	print "<a href='/item_info'>回首頁</a>"
	print "<a href='/admin/item_info.html'>繼續新增資料</a>"
