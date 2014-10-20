#StringProperty(multiline=True)儲存多行資料，不可超過500 bytes。
#BtyeStringProperty()儲存存文字或是二進位資料，與StringProperty不同的地方在於，ByteStringProperty是尚未用文字編碼過的byte資料。
#TextPrpoperty()儲存資料形態為db.Text，無法製作索引、排序及條件比對。
#BooleanProperty()儲存布林值。
#IntegerProperty()儲存整數資料形態。
#FloatProperty()儲存浮點數資料形態。
#DateTimeProperty()、DateProperty()、TimeProperty()使用datetime.datetime、datetime.date、datetime.time物件，選項為：
#auto_now_add：True產生資料時自動加上目前（日期）時間。預設為False。
#auto_now：True自動變更為現在（日期）時間。預設為False。
#ListProperty()、StringListProperty()儲存list資料形態。
#ReferenceProperty()、SelfReferenceProperty()用來指向其他資料實體，儲存資料為db.Key物件。
#UserProperty()儲存Google帳號資料形態。選項為：
#auto_current_user_add：True會自動登入目前的Google帳號，資料更新時，也會自動更新為目前登入的Google帳號。預設為False。
#CategoryProperty()儲存資料形態為db.Category物件。
#LinkProperty()儲存超連結資料，儲存資料為db.Link物件。（會自動驗證格式是否正確）
#EmailProperty()儲存Email格式資料，儲存資料為db.Email物件。（會自動驗證格式是否正確）
#GeoPtProperty()儲存經緯度坐標資料，儲存資料為db.GeoPt物件。
#PhoneNumberProperty()儲存電話號碼格式資料，儲存資料為db.PhoneNumber資料形態。
#PostalAddressProperty()儲存地址格式的資料，儲存資料為db.PostAddress資料形態。
#RatingProperty()儲存評分資料，0~100，儲存資料為db.Rating物件。

from google.appengine.ext import db

#儲存檔案資料
class Photo(db.Model):
	content=db.BlobProperty()
	updated=db.DateTimeProperty(auto_now=True)

#儲存註冊資料
class Register(db.Expando):
	name=db.StringProperty()
	email=db.EmailProperty()

#已有google帳號
class google_user(db.Model):
	account=db.UserProperty()

#相簿資料
class Album(db.Expando):
	title=db.StringProperty(multiline=True) #相簿名稱(utf-8)
	description=db.StringProperty(multiline=True) #註解(utf-8)
	url=db.StringProperty(multiline=True) #檔案櫃網址
	filename=db.StringProperty(multiline=True) #檔案名稱(utf-8)
	dir_name=db.StringProperty(multiline=True)#資料夾名稱(utf-8)

#產品資訊
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

