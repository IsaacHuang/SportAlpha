# -*- coding: utf-8 -*-
from google.appengine.ext import db
import cgi

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
form=cgi.FieldStorage()
count=form.getvalue('count','')
company=form.getvalue('company','')
category=form.getvalue('category','')
Site=form.getvalue('Site','')
series=form.getvalue('series','')
inventory=form.getvalue('inventory','')
pic=form.getvalue('pic','')
Web_url=form.getvalue('Web_url','')
price=form.getvalue('price','')
url=form.getvalue('url','')
item=form.getvalue('item','')
print "<html><meta http-equiv='Content-Type' content='text/html;charset='utf-8'><body>"
link=" "
status="false"
for i in items.all():
	if company==i.company.encode('utf-8'):
		link=i.url
num=0
num=int(count)
num=int(num)
if num==1:
#================================================
	create=items(company=unicode(company,'utf-8'),url=link,filename=unicode(filename,'utf-8'),description=unicode(description,'utf-8'),dir_name=unicode(dir_name,'utf-8'))
	album.put()
	status="true"
elif num>1:
	i=0
	while i<num:
		archive=filename[i]
		if description[i]=="":
			memo=""
		else:
			memo=description[i]
		album=Album(title=unicode(title,'utf-8'),url=link,filename=unicode(archive,'utf-8'),description=unicode(memo,'utf-8'),dir_name=unicode(dir_name,'utf-8'))
		album.put()
		i=int(i)
		i=i+1
		status="true"
if status=="true":
	print "資料已新增！"
else:
	print "資料尚未建立！"
print "<a href='/photo_info'>回首頁</a>"
print "<a href='/book'>繼續新增資料</a>"	
print "</body></html>"	