from socket import *
from tkinter import *
from threading import *

host1 = '127.0.0.1'
port = 5000

class recive(Thread):

	def __init__(self,s):
		Thread.__init__(self)
		self.s = s

	def run(self):
		while True:
			data = self.s.recv(1024)
			if not data : break
			print("\nserver :" + data.decode('ascii'))


class initi(Thread):
	s = socket()

	s.connect((host1,port))

	print("connected to server\n")

	def __init__(self):
		Thread.__init__(self)
		print("threading created\n")
		

	def send(self,*args):
		while True:
			var =input("client>>>:")
			self.s.send(var.encode('ascii'))

	def run(self):
		rec = recive(self.s)
		rec.start()
		self.send()

obj = initi()
obj.start()