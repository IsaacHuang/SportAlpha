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
<form method='post' action='/item_add'>
<fieldset>
			<legend>選擇廠牌</legend>
			<font color=red>必需選擇一家，否則會出現錯誤！</font><br>
"""
link=" "
Num=0
for i in a.run():
	if i.Web_url.encode('utf-8')!=link:
		link=i.Web_url.encode('utf-8')
		print "<input name='choose' type='radio' value='%d'>"%(Num)
		print "%s<br><input name='company' type='text' hidden='true' value='%s'>"%(i.company.encode('utf-8'),i.company.encode('utf-8'))
		print"<input name='Site' type='text' hidden='true' value='%s'>"%(i.Site)#檔案櫃網址
		print"""<input name='Web_url' type='text' hidden='true' value='%s'>
		請輸入檔案個數：<input name='count' type='text' size='3'><br>
		商品類別：<br><input type='text' name='category' size='100'><br>
		"""%(link)#官網網址
		Num=Num+1
print """
<input type='submit' value='新增'>
<input type='reset' value='重新填寫'><br>
<a href='/item_info'>回首頁</a>
</fieldset>
</form>
</body>
</html>
"""