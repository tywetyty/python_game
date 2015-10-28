import socket

solist = [x for x in dir(socket) if x.startswith('SO_')]
solist.sort()
for x in solist:
	print x

result = socket.getaddrinfo('www.google.com', 0)
print result[0]