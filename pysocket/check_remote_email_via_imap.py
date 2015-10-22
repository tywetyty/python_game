import argparse
import getpass
import imaplib
NET_IMAP_SERVER = 'imap.163.com' 
NET_IMAP_PORT=993

def check_email(username): 
	mailbox=imaplib.IMAP4_SSL(NET_IMAP_SERVER,NET_IMAP_PORT)
	password = getpass.getpass(prompt='Enter your 163 password: ')
	mailbox.login(username, password)
	status, msgs=mailbox.select('Inbox')
	print status
	print msgs
	typ,data=mailbox.search(None,'ALL')
	for mun in data[0],split():
		typ,data=mailbox.fetch(num, '(RFC882)')
		print 'Message %s\n%s\n' % (num, data[0][1])
		break
	mailbox.close()
	mailbox.logout()

if __name__ == '__main__':
	parser=argparse.ArgumentParser(description='Email Download Example')
	parser.add_argument('--username',action='store',dest='username',default=getpass.getuser())
	username=parser.parse_args().username
	check_email(username)