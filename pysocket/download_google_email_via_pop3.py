import argparse
import getpass
import poplib

NET_POP3_SERVER = 'pop.163.com'

def download_email(username):
	mailbox=poplib.POP3_SSL(NET_POP3_SERVER,995)
	mailbox.user(username)
	pswd=getpass.getpass(prompt='Enter your Goole password:')
	mailbox.pass_(pswd)
	num_messages=len(mailbox.list()[1])
	print "Total emails: %s" %num_messages
	print "Getting last message" 
	# print mailbox.list()
	# print mailbox.retr(num_messages)[1]
	for msg in mailbox.retr(num_messages)[1]:
		print msg
	mailbox.quit()

if __name__ == '__main__':
	parser=argparse.ArgumentParser(description='Email Download Example')
	parser.add_argument('--username',action='store',dest='username',default=getpass.getuser())
	username=parser.parse_args().username
	download_email(username)