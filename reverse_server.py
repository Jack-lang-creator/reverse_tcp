
import socket
#configure server host
serv_host = "127.0.0.1"
#configure server port
serv_port = 5001
buffer = 1024
s = socket.socket()
#bind the ip with port
s.bind((serv_host,serv_port))
#listen for connections
s.listen(5)
print(f"Listening as {serv_host}:{serv_port} ...")
client_socket = s.accept()
client_addr = s.accept()
#message = "hello World".encode()
#client_socket.send(message)
print(f"{client_addr[0]}:{client_addr[1]} Connected!")
while True:
   command = input("Enter the command: ")
   client_socket.send(command).encode()
   if command == "exit":
      break
   result = client_socket.recv(buffer).decode()
   print(result)
#close client connections   
client_socket.close()
#close server connection
s.close()

