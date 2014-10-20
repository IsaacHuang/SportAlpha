# -*- coding: utf-8 -*-
from google.appengine.ext import db

class Album(db.Expando):
	title=db.StringProperty(multiline=True) #相簿名稱
	description=db.StringProperty(multiline=True) #註解
	url=db.StringProperty(multiline=True) #檔案櫃網址
	filename=db.StringProperty(multiline=True) #檔案名稱
	dir_name=db.StringProperty(multiline=True)#資料夾名稱

a=db.GqlQuery("select * from Album order by title DESC")
print "<html><meta http-equiv='Content-Type' content='text/html;charset=utf-8'><body>"
print """
	<table border='1'>
		<form action='/Photo_Remove' method='post'>
		<tr>
			<td></td>
			<td>相簿名稱</td>
			<td>資料夾名稱</td>
			<td>檔案名稱</td>
			<td>圖片</td>
		"""
count=0
for i in a.run():
	print"""
			<tr>
				<td>
					<input name='choose' type='checkbox' value='%d'>
					<input name='photo_delete' type='text' hidden='true' value='%s'>
				</td>
				"""%(count,i.url)
	print """<td>
				%s	
			</td>"""%(i.title.encode('utf-8'))
	if i.dir_name is None:
		print "<td>No folder</td>"
	else:
		print "<td>%s</td>"%(i.dir_name.encode('utf-8'))
	print "<td><input name='photo_file' hidden='true' type='text' value='%s'>%s</td>"%(i.filename.encode('utf-8'),i.filename.encode('utf-8'))
	print "<td><a href=%s/%s target='_blank'><img src=%s/%s height=50></a></td>"%(i.url,i.filename.encode('utf-8'),i.url,i.filename.encode('utf-8'))
	print "<td><input type='submit' value='刪除'></td>"
	print "</tr>"
	count=count+1

print "</form></table>"
print "</body></html>"