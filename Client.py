import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostName = socket.gethostname() #change this IP adress to the WIFI LAN IPV4 to connect two devices over wifi
port = 5733


try:
    s.connect((hostName, port))
except:
    print('Connection Failed')
    exit()

print("This program acts as an interface with a server that offers the following commands:\n\n 1.return the ID of an existing user (input ex. user1ID)\n 2.return the hashed value of a string (input ex. md5Hello There!)\n 3. check if you're lucky (input ex. am I lucky!)\n ")
command = input("enter a command:\n")

if command.endswith("ID") or command.startswith("md5") or command == "am I lucky!":
    s.send(command.encode("ascii"))
    msgFromServer = s.recv(1024)
    print(msgFromServer.decode('ascii'))

else:
    print("Command Recieved was incorrect")

s.close()


