# -*- coding: utf-8 -*-
from google.appengine.ext import db
import cgi
form=cgi.FieldStorage()
name=form.getvalue('name','')
email=form.getvalue('email','')
password=form.getvalue('password','')
print name
print email
print password
class Register(db.Expando):
	name=db.StringProperty()
	email=db.StringProperty()
	password=db.StringProperty()

reg=Register(name=name,email=email,password=password)
reg.put()
print"""
<html>
<head><meta http-equiv='Content-Type' content='text/html;charset=utf-8'></head>
<body>
<h1>您註冊資料如下</h1>
<ul>
<li>您的大名：%s</li>
<li>您的Email：%s</li>
</ul>
"""% (name,email)
query=db.GqlQuery("SELECT * FROM Register")
count=0
count=int(count)
for i in Register.all():
	print "Name:%s,email:%s<br>"%(i.name,i.email)
	count=count+1

print "共 %s筆資料！" %(count)