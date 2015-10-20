import socket 
import select 
import argparse 
import diesel
SERVER_HOST = 'localhost' 
 
EOL1 = b'\n\n' 
EOL2 = b'\n\r\n' 
SERVER_RESPONSE  = b"""HTTP/1.1 200 OK\r\nDate: Mon, 1 Apr 2013 01:01:01 
GMT\r\nContent-Type: text/plain\r\nContent-Length: 25\r\n\r\n 
Hello from Epoll Server!""" 

print SERVER_RESPONSE 