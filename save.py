# -*- coding: utf-8 -*-
from google.appengine.ext import db
import cgi

class Album(db.Expando):
	title=db.StringProperty(multiline=True) #相簿名稱
	description=db.StringProperty(multiline=True) #註解
	url=db.StringProperty(multiline=True) #檔案櫃網址
	filename=db.StringProperty(multiline=True) #檔案名稱
	dir_name=db.StringProperty(multiline=True)#資料夾名稱
a=db.GqlQuery("select * from Album order by title DESC")
form=cgi.FieldStorage()
title=form.getvalue('title','')
count=form.getvalue('count','')
filename=form.getvalue('filename','')
description=form.getvalue('description','')
dir_name=form.getvalue('dir_name','')
print "<html><meta http-equiv='Content-Type' content='text/html;charset='utf-8'><body>"
if title=="":
	print "請選擇相簿！"
	print "<a href='/book'>回上一頁</a>"
if count=="":
	print "請輸入檔案數！"
	print "<a href='/book'>回上一頁</a>"
link=" "
status="false"
for i in Album.all():
	if title==i.title.encode('utf-8'):
		link=i.url
num=0
num=int(count)
num=int(num)
print "dir_name:%s"%(dir_name)
if num==1:
	album=Album(title=unicode(title,'utf-8'),url=link,filename=unicode(filename,'utf-8'),description=unicode(description,'utf-8'),dir_name=unicode(dir_name,'utf-8'))
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
