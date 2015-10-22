import urllib
import os
from sys import exit

TARGET_URL = 'http://python.org/ftp/python/2.7.4/' 
TARGET_FILE = 'Python-2.7.4.tgz' 

class CustomURLOpener(urllib.FancyURLopener):
	def http_error_206(self,url,fp,errcode,errmsg,header,data=None):
		pass
def resume_download():
	file_exists =0
	CustomURLClass=CustomURLOpener()
	if os.path.exists(TARGET_FILE):
		out_file=open(TARGET_FILE,'ab')
		file_exists=os.path.getsize(TARGET_FILE)
		CustomURLClass.addheader('range','bytes=%d-' % (file_exists))
	else:
		out_file=open(TARGET_FILE,'wb')
	web_page=CustomURLClass.open(TARGET_URL+TARGET_FILE)
	print file_exists
	if int(web_page.headers['Content-Length'])==file_exists:
		loop=0
		print "File already downloaded!" 
		exit()
	byte_count=0
	while True:
		data=web_page.read(8192)
		if not data:
			break
		out_file.write(data)
		byte_count+=len(data)
	web_page.close()
	out_file.close()
	print byte_count
	for k,v in web_page.headers.items():
		print k,'=',v
	print  "File copied", byte_count, "bytes from", web_page.url

if __name__ == '__main__':
	resume_download()