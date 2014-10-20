# -*- coding: utf-8 -*-
from google.appengine.ext import db
import cgi
form=cgi.FieldStorage()
account=form.getvalue('account','')
password=form.getvalue('password','')

class Register(db.Expando):
	name=db.StringProperty()
	email=db.StringProperty()
	password=db.StringProperty()
a=db.GqlQuery("select * from Register order by email DESC")
for i in a.run():
	if account==i.email and password==i.password:
		print "<script>document.cookie='visit=administrator';document.location.href='/admin/admin_index.html'</script>"
	else:
		print "<script>document.location.href='/admin'</script>"