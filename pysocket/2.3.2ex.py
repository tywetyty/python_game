import os
import sys
import socket
import threading
import SocketServer

SERVER_HOST='localhost'
SERVER_PORT=0
BUF_SIZE=1024
ECHO_MSG='Hello echo server!'

def client(ip,port,message):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((ip,port))
	try:
		sock.send(message)
		response=sock.recv(BUF_SIZE)
		print 'Client received: %s' % response 
	finally:
		sock.close()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		data=self.request.recv(BUF_SIZE)

		print 'Server received: %s' %data
		current_thread=threading.currentThread()
		response='%s:%s' % (current_thread.name,data)
		self.request.sendall(response)
class ThreadedTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):pass

def main():
	server=ThreadedTCPServer((SERVER_HOST,SERVER_PORT), ThreadedTCPRequestHandler)
	ip,port=server.server_address
	server_thread=threading.Thread(target=server.serve_forever)
	server_thread.daemon=True
	server_thread.start()
	print 'Server loop running on thread: %s' %server_thread.name
	client(ip, port, 'Hello from client 1')
	client(ip, port, 'Hello from client 2')
	client(ip, port, 'Hello from client 3')
	server.shutdown()


if __name__ == '__main__':
	main()
