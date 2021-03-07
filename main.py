#Replace the binding IP with your system IP before running the code 
#POrt can also be specified accordingly 

import socket
import threading
import time
import os

ip = input("Enter the IP of reciever: ")
person = input("Enter the name of reciever: ")
print("\n\n Enter the text to send while to command prompt is waiting ......")
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

s.bind(("192.168.43.191", 567))

def receive() :
    while True : 
        data = s.recvfrom(1024)
        os.system("tput setaf 3")
        out = str(data[0])
        print(person + ":" + out[1:])
        os.system("tput setaf 7")

def send() :
    msg = None  
    while True :
        msg = input()
        def sent(msg) :
            s.sendto( msg.encode() , (ip,567))
        sent(msg)
        time.sleep(0.0000001)

x1=threading.Thread(target=receive)
x2=threading.Thread(target=send)

x1.start()
x2.start()

