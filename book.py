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
print"""
<html>
<meta equiv-http='Content-Type' content="text/html;charset='utf-8'">
<head>
<style>
	a{
		font-size: 20;
		font-family: "標楷體";
		color: red;
	}
</style>
</head>
<body>
<form method='post' action='photo_add'>
<fieldset>
			<legend>選擇相簿</legend>
"""
link=" "
Num=0
for i in a.run():
	if i.url!=link:
		Num=int(Num)
		Num=Num+1
		Num=str(Num)
		print """<input name='title' type='radio' value='%s'>%s<br>
		請輸入檔案個數：<input name='count' type='text' size='3'><br>
		資料夾名稱：<br><input type='text' name='dir_name' size='100' value='No folder'><br>
		"""%(i.title.encode('utf-8'),i.title.encode('utf-8'))
		link=i.url
print """
<input type='submit' value='新增'><input type='reset' value='重新填寫'><br>
<a href=/photo_info>回首頁</a>
</fieldset>
</form>
</body>
</html>
"""