import sys
import os.path
import uuid
from glob import glob
from datetime import datetime
import os

class HttpServer:
	def __init__(self):
		self.sessions={}
		self.types={}
		self.types['.pdf']='application/pdf'
		self.types['.jpg']='image/jpeg'
		self.types['.txt']='text/plain'
		self.types['.html']='text/html'

	def response(self,kode=404,message='Not Found',messagebody='',headers={}):
		tanggal = datetime.now().strftime('%c')
		resp=[]
		resp.append("HTTP/1.0 {} {}\r\n" . format(kode,message))
		resp.append("Date: {}\r\n" . format(tanggal))
		resp.append("Connection: close\r\n")
		resp.append("Server: myserver/1.0\r\n")
		resp.append("Content-Length: {}\r\n" . format(len(messagebody)))
		for kk in headers:
			resp.append("{}:{}\r\n" . format(kk,headers[kk]))
		resp.append("\r\n")
		resp.append("{}" . format(messagebody))
		response_str=''
		for i in resp:	
			response_str="{}{}" . format(response_str,i)
		return response_str

	def proses(self,data):		
		requests = data.split("\r\n")

		baris = requests[0]
		semua_header = [n for n in requests[1:] if n!='']

		j = baris.split(" ")
		print("\nDEBUG\n")
		print(semua_header)
		print("\n\n")
		try:
			method = j[0].upper().strip()
			# Jika menerima method GET
			if (method=='GET'):
				object_address = j[1].strip()
				return self.http_get(object_address, semua_header)
			# Jika menerima method POST
			elif (method=='POST'):
				object_address = j[1].strip()
				return self.http_post(object_address, semua_header)
			else:
				return self.response(400,'Bad Request','',{})
		except IndexError:
			return self.response(400,'Bad Request','',{})

	def http_get(self,object_address,headers):
		files = glob('./*')
		direktori = '.'

		# Kalau filenya gak terdeteksi (buat handler)
		if direktori + object_address not in files:
			return self.response(404,'Not Found','',{})

		fpath = open(direktori + object_address,'r')

		output = fpath.read()
		fext = os.path.splitext(direktori + object_address)[1]

		try:
			content_type = self.types[fext]
		except KeyError:
			return self.response(404, 'Not found', '', {})

		headers = {}
		headers['Content-type'] = content_type
		
		return self.response(200,'OK',output,headers)

	def http_post(self,object_address,headers):
		request = headers[-1]
		respon = request.split("=")
		output = respon[1]
		headers={}

		return self.response(200,'OK',output,headers)
