# -*- coding: utf-8 -*-
import cgi

form=cgi.FieldStorage()
count=form.getvalue('count','')#檔案個數
company=form.getvalue('company','')
category=form.getvalue('category','')
Site=form.getvalue('Site','')
Web_url=form.getvalue('Web_url','')
choose=form.getvalue('choose','')
print """<html>
<meta http-equiv='Content-Type' content="text/html;charset='utf-8'">
<body>
<form method='post' action='/item_save'>
<fieldset id='Info_form'>
<legend>新增資料</legend>
<table id='info_table'>
"""
num=0
if count != "":
	num=count
	num=int(num)
else:
	print "請輸入檔案個數！"
	print "<a href='/category'>回上一頁</a>"
if category=="":
	print "請輸入商品類別！"
	print "<a href='/category'>回上一頁</a>"
choose=int(choose)
com=company[choose]#品牌名稱
cat=category#商品類別
Sit=Site[choose]#檔案櫃網址
Web=Web_url[choose]#官網網址
i=1
while i<=num:
	print"""
	<tr>
		<td>
		新增資料_%d
		</td>
		<td>
		</td>
	</tr>
	<tr>
		<td>
		商品名稱：
		</td>
		<td>
			<input type='text' name='item' size='50'>
		</td>
	</tr>
	<tr>
		<td>
		商品型號：
		</td>
		<td>
			<input type='text' name='series' size='100'>
		</td>
	</tr>
	<tr>
		<td>
		商品官網網址：
		</td>
		<td>
			<input type='text' name='url' value='No url' size='100'>
		</td>
	</tr>
	<tr>
		<td>
		圖檔名稱：
		</td>
		<td>
			<input type='text' name='pic' value='No pic' size='50'>
		</td>
	</tr>
	<tr>
		<td>
		價位：
		</td>
		<td>
			<input type='text' name='price' value='0' size='5'>
		</td>
	</tr>
	<tr>
		<td>
		庫存：
		</td>
		<td>
			<input type='text' name='inventory' value='1' size='10'>
		</td>
	</tr>
	"""%(i)
	i=i+1
print"""
	</table>
</fieldset>
<input type='text' name='company' value='%s' hidden='true'>
<input type='text' name='category' value='%s' hidden='true'>
<input type='text' name='Site' value='%s' hidden='true'>
<input type='text' name='Web_url' value='%s' hidden='true'>
<input type='text' name='count' value='%s' hidden='true'>
<input type='submit' value='新增'>
<input type='reset' value='重新填寫'><br>
</form>
<div>
<a href="/category">回上一頁</a>
</div>
</body>
</html>
"""%(com,cat,Sit,Web,count)
