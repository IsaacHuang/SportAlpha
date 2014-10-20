# -*- coding: utf-8 -*-
from google.appengine.ext import db

class Album(db.Expando):
	title=db.StringProperty(multiline=True) #相簿名稱
	description=db.StringProperty(multiline=True) #註解
	url=db.StringProperty(multiline=True) #檔案櫃網址
	filename=db.StringProperty(multiline=True) #檔案名稱
	dir_name=db.StringProperty(multiline=True)#資料夾名稱
a=db.GqlQuery("select * from Album order by title DESC")
for i in a.run():
	print "<html><meta http-equiv='Content-Type' content='text/html;charset=utf-8'><body>"
	print "<p>相簿名稱：%s<br>"%(i.title.encode('utf-8'))
	if i.dir_name is None:
		print "檔案名稱：%s<br>"%(i.filename.encode('utf-8'))
		print "<a href=%s/%s target='_blank'><img src=%s/%s height=50></a></p>"%(i.url,i.filename.encode('utf-8'),i.url,i.filename.encode('utf-8'))
	else:
		print "資料夾名稱：%s<br>"%(i.dir_name.encode('utf-8'))
		print "檔案名稱：%s<br>"%(i.filename.encode('utf-8'))
		print "<a href=%s/%s target='_blank'><img src=%s/%s height=50></a></p>"%(i.url,i.filename.encode('utf-8'),i.url,i.filename.encode('utf-8'))
print "</body></html>"