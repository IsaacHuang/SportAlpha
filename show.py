# -*- coding: utf-8 -*-
from google.appengine.ext import db

class Album(db.Expando):
	title=db.StringProperty(multiline=True) #相簿名稱
	description=db.StringProperty(multiline=True) #註解
	url=db.StringProperty(multiline=True) #檔案櫃網址
	filename=db.StringProperty(multiline=True) #檔案名稱
	dir_name=db.StringProperty(multiline=True)#資料夾名稱

a=db.GqlQuery("select * from Album order by title DESC")
print """<HTML>
<HEAD>
	<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
<TITLE></TITLE>
<script type="text/javascript" src="http://www.google.com/jsapi"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js">
	</script>
	<script>
	var book=new Array();"""
book_num=0
dir_num=0
entity=0
book_name=""
Dir_name=""
for i in a.run():
	if book_name != i.title.encode('utf-8'):
		book_name=i.title.encode('utf-8')
		print """book[%d]="%s";"""%(book_num,book_name)
		book_num=book_num+1
		b=db.GqlQuery("select * from Album where title=:1",unicode(book_name,'utf-8'))
		print "var dir_book%d=new Array();"%(book_num)
		print "var book%d_file_url=new Array();"%(book_num)
		for j in b.run():
			if j.dir_name is None:
				Dir_name="No folder !"
			elif Dir_name != j.dir_name.encode('utf-8'):
				Dir_name=j.dir_name.encode('utf-8')
				print """dir_book%d[%d]="%s";"""%(book_num,dir_num,Dir_name)
				dir_num=dir_num+1
				c=db.GqlQuery("select * from Album where title=:1 and dir_name=:2",unicode(book_name,'utf-8'),unicode(Dir_name,'utf-8'))
				for j in c.run():
					s="book%d_file_url[%d]=%s/%s"%(book_num,entity,j.url,j.filename.encode('utf-8'))
					print s
					entity=entity+1
		if Dir_name=="No folder !":
			print """dir_book%d[%d]="No folder!";"""%(book_num,dir_num)
			dir_num=dir_num+1
		c=db.GqlQuery("select * from Album where title=:1",unicode(book_name,'utf-8'))
		for j in c.run():
			if j.dir_name is None:
				s="book%d_file_url[%d]=%s/%s"%(book_num,entity,j.url,j.filename.encode('utf-8'))
				print s
				entity=entity+1
		print """
		function NavBlock(){

		}
		"""
	dir_num=0
	entity=0
print """
function setZ( o, level )
{
  o.style.zIndex=level;
}
</script>
<style>
.crp {
	font-size:0px;
    line-height:0;
    width:70%;
    height:95%;
    overflow:hidden;
     }
.crp img
    {
    position:relative;
    padding:0px;
    margin:0px;
    width:100%;
    height:100%;
    border:none;
    outline:none;
    }
.crp div{
	position:relative;
    top:-100%;
    height:100%;
    background:white;
    color:black;
    font-size:20px;
    line-height:1.2;
}
#show{
	display:none;
	text-align: center;
	}
</style>
<body>
<marquee behavior="scroll" height="5%"><font color='purple'>此相簿為私人照片，不提供轉載及商業用途，如有違法，自負法律責任！</font></marquee>
<div id="nav" style="float:left;width:10%;"></div>
<div id="log" style="float:up;width:10%;height:10%;">
		<form method="post" action='/pass'>
			請輸入您的通關碼，方可下載私人圖片：<br>
			<input type="text" size="10">
		</form>
	</div>
	<div id="shut" style="float:right;width:5%;height:20%;color:blue;background-color:yellow;font-size:30;">關閉圖片</div>
<center><div class=crp id="show">
<img  name="imgs" id="imgs" onload='setZ(this, 2)'
  onmouseover='setZ(this, -2)'
  onmouseout='setZ(this, 2)'src="/img/yellow_logo.png">
<div onmouseover='setZ(this, 4)'
     onmouseout='setZ(this, 0)' >
請尊重肖像權，本圖不提供下載！<br>
平板手機如誤觸，請點擊logo！
</div>
</div></center>
</body>
</html>
"""