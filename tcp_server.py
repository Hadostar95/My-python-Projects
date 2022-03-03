import socket
from datetime import datetime


HOST='192.168.1.236'
Port = 50008
max_size=1024

sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((HOST,Port))


print("Starting Chatroom...........................")
print('Starting this server at ',datetime.now())
print("Waiting for connection from client")

sock.listen(5)

client,address=sock.accept()

while True:
    data = client.recv(max_size)
    if data.decode('utf-8')=='q':
        break
    print("At: ",datetime.now(),address,"This address says\n",data.decode('utf-8'))
    message_to_client=input("Type your message to Client:   ")
    message_to_client_encoded=message_to_client.encode('utf-8')
    client.send(message_to_client_encoded)
    if message_to_client == 'q':
        break
client.close()    
sock.close()
    

