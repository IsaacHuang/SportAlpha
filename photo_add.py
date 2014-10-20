# -*- coding: utf-8 -*-
import cgi

form=cgi.FieldStorage()
title=form.getvalue('title','')
count=form.getvalue('count','')
dir_name=form.getvalue('dir_name','')
print """<html>
<meta http-equiv='Content-Type' content="text/html;charset='utf-8'">
<body>
<form method='post' action='/save'>
<fieldset id='Info_form'>
			<legend>新增資料</legend>
	<table id='info_table'>
	<tr>
		<td>
		檔案名稱：
		</td>
		<td>
		註解：
		</td>
	</tr>
"""

num=0
if count != "":
	num=count
	num=int(num)
else:
	print "請輸入檔案個數！"
	print "<a href='/book'>回上一頁</a>"
i=1
Dir=dir_name[num]
while i<=num:
	print"""
	<tr>
		<td>
		<input type='text' name='filename'>
		<font color='red'>需輸入副檔名（如：.jpg /.png）</font>
		</td>
		<td>
		<input type='text' name='description' value='No description'>
		</td>
	</tr>
	"""
	i=int(i)
	i=i+1
print"""
	</table>
</fieldset>
<input type='text' name='title' value='%s' hidden='true'>
<input type='text' name='count' value='%s' hidden='true'>
<input type='text' name='dir_name' value='%s' hidden='true'>
<input type='submit' value='新增'>
<input type='reset' value='重新填寫'><br>
</form>
<div>
<a href="/book">回上一頁</a>
</div>
</body>
</html>
"""%(title,count,Dir)