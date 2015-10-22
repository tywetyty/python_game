import os
import argparse
import smtplib
import zipfile
import tempfile
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL

def email_dir_zipped(sender, recipient):
	zf=tempfile.TemporaryFile(prefix='mail',suffix='.zip')
	zipf=zipfile.ZipFile(zf,'w')
	print "Zipping current dir: %s" %os.getcwd()
	for file_name in os.listdir(os.getcwd()):
		zipf.write(file_name)
	zipf.close()
	zf.seek(0)
	print zf,zipf
	print "Creating email message..."
	print os.getcwd()[-1]+'.zip'
	email_msg=MIMEMultipart()
	email_msg['Subject']='File from path %s' %os.getcwd()
	email_msg['To']=','.join(recipient)
	email_msg['From']=sender
	msg=MIMEBase('application','zip')
	msg.set_payload(zf.read())
	encoders.encode_base64(msg)
	msg.add_header('Content-Disposition','attachment', file_name=os.getcwd()[-1]+'.zip')
	email_msg.attach(msg)
	email_msg=email_msg.as_string()
	print "Sending email message..."
	smtp=SMTP_SSL('smtp.163.com',465)
	try:
		smtp.login(sender, '51553963')
		smtp.set_debuglevel(1)
		smtp.sendmail(sender,recipient, email_msg)
	except Exception, e:
		print 'Error: %s' %str(e)
	finally:
		smtp.close()

if __name__ == '__main__':
	parser=argparse.ArgumentParser(description='Email Example')
	parser.add_argument('--sender',action='store',dest='sender',default='mazhouliang_1@163.com')
	parser.add_argument('--recipient',action='store',dest='recipient',default='306708403@qq.com')
	given_args=parser.parse_args()
	email_dir_zipped(given_args.sender, given_args.recipient)
