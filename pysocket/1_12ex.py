import ntplib
from time import ctime
import socket
import struct
import sys
import time
NTP_SERVER = "0.uk.pool.ntp.org" 
TIME1970 = 2208988800L 
def print_time():
	ntp_client=ntplib.NTPClient()
	response=ntp_client.request('10.10.10.42')
	print ctime(response.tx_time)
def sntp_client():
	client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	data='\x1b' + 47 * '\0' 
	client.sendto(data,(NTP_SERVER,123))
	data,address=client.recvfrom(1204)
	if data:
		print 'Response received from:', address 
	t=struct.unpack('!12I', data )[10]
	t-=TIME1970
	print '\tTime=%s' % time.ctime(t) 
if __name__ == '__main__':
	sntp_client()