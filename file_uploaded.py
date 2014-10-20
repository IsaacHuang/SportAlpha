from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers

upload_url=blobstore.create_upload_url('/upload')
print "<html><meta http-equiv='Content-Type' content='text/html;charset=UTF-8'><body><form action='%s' method='post' enctype='multipart/form-data'>" %(upload_url)
print "UploadFile: <input type='file' name='file'><br><input type='submit' name='submit' value='Submit'>"
print "</form></body></html>"