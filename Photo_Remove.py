# -*- coding: utf-8 -*-
from google.appengine.ext import db

class Album(db.Expando):
	title=db.StringProperty(multiline=True) #相簿名稱
	description=db.StringProperty(multiline=True) #註解
	url=db.StringProperty(multiline=True) #檔案櫃網址
	filename=db.StringProperty(multiline=True) #檔案名稱
	dir_name=db.StringProperty(multiline=True)#資料夾名稱
import cgi
form=cgi.FieldStorage()
photo_delete=form.getvalue('photo_delete','')
photo_file=form.getvalue('photo_file','')
count=form.getvalue('choose','')
for i in Album.all():
	for a in count:
		a=int(a)
		if i.url==photo_delete[a]:
			if i.filename.encode('utf-8')==photo_file[a]:
				Album.delete(i)

print "<script>document.location.href='/return_page'</script>"