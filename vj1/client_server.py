
import socket
import _thread
import time

def start_server():
    IP = '127.0.0.1'
    PORT = 40101
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen()
    return s

def connect_to_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 40102))
    return s


serversocket=start_server()

def recv_msg(client):
    msg = client.recv(1024).decode()
    print(msg)

def send_msg(clientsocket,sender):
    count = 1
    msg="different"
    prev_msg=''
    while(prev_msg!=msg):
        _thread.start_new_thread(recv_msg, (sender,))
        if (count==1):
            msg=input()
            count -=1
        clientsocket.sendall(str.encode(msg))
        prev_msg=msg
        msg=input()
    return
        

pokusaj = 10
while pokusaj > 0:
    try:
        clientsocket = connect_to_server()
        sender, address = serversocket.accept()
        send_msg(clientsocket,sender)
        break
    except socket.error as error:
        print(error, "\n novi pokusaj za 5 sekundi (", pokusaj, "pokusaja je ostalo )")
        time.sleep(5)
    pokusaj -= 1
