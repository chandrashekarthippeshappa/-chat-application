from socket import *
from  threading import *

host1 = "127.0.0.1"
port = 5000

class recvie(Thread):
	def __init__(self,s,con):
		Thread.__init__(self)

		self.con = con 
		self.s = s

	def run(self):
		while True:
			data = self.con.recv(1024)
			if not data : break
			print("\nclient :" + data.decode('ascii'))

class initi(Thread):

	s = socket()
	s.bind((host1,port))
	s.listen(1)
	print("Waiting for the other party to join: ")
	con,addr  =s.accept()
	print("\nConnected to client %s\n" % con)

	def __init__(self):
		Thread.__init__(self)
		

	def send(self,*args):
		while True :
			var =input("server>>> ")
			self.con.send(var.encode('ascii'))

	def run(self):
		rec = recvie(self.s,self.con)
		rec.start()
		self.send()





obj = initi()
obj.start()