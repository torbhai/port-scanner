#!/user/bin/python
print ('''created and developed by tor bhai studio. visit us on our site to learn hacking , programming, web developement and many more for free.
https://torbhai.in ''')
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tip = input ("input victims[ target ] ip  ")
tport = input ("input the port  ")
def torscanner(tport):
	if sock.connect_ex({tip,tport}):
		print ("the %d port is closed") %(tport)
	else:
		print ('the %d port is open') %(tport)
torscanner(tport)
