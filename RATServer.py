import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, add = s.accept()
    with conn:
        while True:
            command = input("Your command: ")
            if(command == exit):
                print("Bye ")
                break
            else:
                conn.sendall(str.encode(command))
                #sleep(2000)
                data = conn.recv(2048)
                print("Recieved :" , data.decode())

