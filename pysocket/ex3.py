import socket

SEND_BUF_SIZE = 4096 
RECV_BUF_SIZE = 4096
def modify_buff_size():
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	bufszie=sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print "Buffer size [Before]:%d" % bufszie
	sock.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUF_SIZE)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RECV_BUF_SIZE)
	bufszie=sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print "Buffer size [After]:%d" % bufszie 


if __name__ == '__main__':
	modify_buff_size()