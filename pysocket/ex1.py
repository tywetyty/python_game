import socket
from binascii import hexlify
host_name=socket.gethostname()
print host_name
host_ip =socket.gethostbyname('WIN-9493D21Q4KG')
print host_ip
def get_ramote_ip():
	romote_host='www.pytgo.org'
	try:
		print socket.gethostbyname(romote_host)
	except socket.error, error_msg:
		raise error_msg
def convert():
	data=1234
	print "Original: %s => Long host byte order: %s, Network byte order: %s"\
	%(data,socket.ntohl(data),socket.htonl(data))
def test_socket_timeout():
	s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print "Default socket timeout: %s" % s.gettimeout()
	s.settimeout(100)
	print "Default socket timeout: %s" % s.gettimeout()
if __name__ == '__main__':
	get_ramote_ip()
	packed_ip_addr=socket.inet_aton('127.0.0.1')
	print hexlify(packed_ip_addr)
	print socket.inet_ntoa(packed_ip_addr)
	convert()
	test_socket_timeout()
