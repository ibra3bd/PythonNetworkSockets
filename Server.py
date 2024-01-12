import socket
import random as r
import hashlib

#initiating a socket and listening for connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostName = socket.gethostname()  #getting the server host IP
port = 5733  #server port (can be changed)
s.bind((hostName, port))
s.listen(5)



def returnUserID(username):
    obtainedID = "User not found" #initiation is not found by default (unless otherwise)
    try: 
        with open('/etc/passwd', 'r') as passwd_file:
            for line in passwd_file:
                fields = line.strip().split(':')
                if fields[0] == username:
                    obtainedID = fields[2]  #User ID is the third field [index of 2] in /etc/passwd
    except:
        return "Server Error: Failed to open the passwd file"
        exit()
        
    return obtainedID




def returnMD5Hashing(stringExtracted):
    randomNum = r.randint(1, 100)
    return hashlib.md5((stringExtracted + str(randomNum)).encode('ascii')).hexdigest()
    


def returnLuck():
    arr = ['yes','no']
    return r.choice(arr)





while True:

    #establishing connection
    clientSocket, address = s.accept()
    print("Connection from %s has been established." % (str(address)))

    #recieving command and decoding it
    commandReceived_data = clientSocket.recv(1024)
    clientCommand = commandReceived_data.decode("ascii")

    if clientCommand.endswith("ID"):
        usernameExtracted = clientCommand[:len(clientCommand)-2]
        clientSocket.send(returnUserID(usernameExtracted).encode('ascii'))
        
    elif clientCommand.startswith("md5"):
        stringExtracted = clientCommand[3:]
        clientSocket.send(returnMD5Hashing(stringExtracted).encode('ascii'))    

    elif clientCommand == "am I lucky!":
        clientSocket.send(returnLuck().encode('ascii'))
    
    else:
        clientSocket.send("Server Error: Command recieved by the client is not compatable".encode('ascii'))
        print("Server Error: Command recieved by the client is not compatable") 


    clientSocket.close()
    exit()
