import socket
from datetime import datetime

HOST='192.168.1.236'
Port = 50008
max_size=1024



print("Starting Chatroom...........................")
print('Starting this client at ',datetime.now())
print("Waiting for connection to server")
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,Port))


while True:
    message_to_server=input("Type your message to Server:    ")
    message_to_server_encoded=message_to_server.encode('utf-8')
    s.send(message_to_server_encoded)
    if message_to_server =='q':
        break
    data=s.recv(max_size)
    if data.decode('utf-8')=='q':
        break
    print("At",datetime.now(),"Server relpied with: ",data.decode('utf-8'))

s.close()
    
