from socket import *
class UDP():  
	udp_socket = socket(AF_INET, SOCK_DGRAM)
	client_addr = (0,0)	
	
	def __init__(self, addr):
		UDP.udp_socket.bind(addr)

	def recv(self):
		UDP.udp_socket.settimeout(1)
		try:
			self.data = UDP.udp_socket.recvfrom(1024)
		except: 
			return bytes("", encoding = 'utf-8')
		UDP.client_addr = self.data[1]
		print('client addr: ', self.data[1])
		print('recieved: ', self.data[0])
		return self.data[0]
		
	def pos_array(self,_recv_arr):
		return [i for i, n in enumerate(_recv_arr) if n == 59]
		
	def send(self, msg):
		self.msg = bytes(msg, encoding = 'utf-8')
		UDP.udp_socket.sendto(self.msg, UDP.client_addr)

	def stop_listening(self):  
		UDP.udp_socket.close()
		
