# -*- coding: utf-8 -*-
from google.appengine.ext import db
import cgi
form=cgi.FieldStorage()
title=form.getvalue('title','')
description=form.getvalue('description','')
Site=form.getvalue('Site','')
filename=form.getvalue('filename','')
dir_name=form.getvalue('dir_name','')
if description is None:
	description="No description"
if dir_name is None:
	dir_name="No folder"
class Album(db.Expando):
	title=db.StringProperty(multiline=True) #相簿名稱
	description=db.StringProperty(multiline=True) #註解
	url=db.StringProperty(multiline=True) #檔案櫃網址
	filename=db.StringProperty(multiline=True) #檔案名稱
	dir_name=db.StringProperty(multiline=True)#資料夾名稱
judge=""
a=db.GqlQuery("select * from Album order by title DESC")
for i in a.run():
	if title==i.title.encode('utf-8'):
		print "此相簿已存在！"
		judge="此相簿已存在！"
		print "<a href='/photo_info'>回首頁</a>"
		print "<a href='/admin/photo_info.html'>繼續新增資料</a>"
		break
if judge!="此相簿已存在！":
	album=Album(title=unicode(title,'utf-8'),description=unicode(description,'utf-8'),url=Site,filename=unicode(filename,'utf-8'),dir_name=unicode(dir_name,'utf-8'))
	album.put()
	print "資料已新增！"
	print "<a href='/photo_info'>回首頁</a>"
	print "<a href='/admin/photo_info.html'>繼續新增資料</a>"
