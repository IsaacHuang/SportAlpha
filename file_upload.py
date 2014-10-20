# -*- coding: utf-8 -*-
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
import webapp2

class Photo(db.Model):
	blob_key=blobstore.BlobReferenceProperty()

class Upload_photo(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		upload=self.get_uploads()[0]
		files=Photo(blob_key=upload.key())	

for img in Photo.all():
	data=Photo.open(img.key)
	print data