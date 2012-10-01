import socket

HOST = raw_input("Enter the IP to be scanned:")
PORT = 1

for PORT in range(1, 1025):
#	print "Checking for port no. : ", PORT
	socket.setdefaulttimeout(0.5)
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		mysocket.connect((HOST, PORT), )
	except socket.error, msg:
		#print msg
		mysocket.close()
		mysocket = None
		try:
			print PORT, socket.getservbyport(PORT), "down"
		except socket.error, msg:
			print "UNKNOWN PORT", "down"
		continue
	except socket.timeout, msg:
		mysocket.close()
                mysocket = None
                try:
                        print PORT, socket.getservbyport(PORT), "down"
                except socket.error, msg:
                        print "UNKNOWN PORT", "down"

		continue
	
	print PORT, socket.getservbyport(PORT), "up"
	mysocket.close()
	mysocket = None

