import urllib
import os

TARGET_URL = 'http://python.org/ftp/python/2.7.4/' 
TARGET_FILE = 'Python-2.7.4.tgz' 

class CustomURLOpener(urllib.FancyURLopener):
	def http_error_206(self,url,fp,errcode,errmsg,header,data=None):
		pass
def resume_download():
	file_exists =False
	CustomURLClass=CustomURLOpener()
	if os.path.exists(TARGET_FILE):
		out_file=open(TARGET_FILE,'ab')
		file_exists=os.path.getsize(TARGET_FILE)
		CustomURLClass.addheader('range','bytes=%s-' % (file_exists))
	else: