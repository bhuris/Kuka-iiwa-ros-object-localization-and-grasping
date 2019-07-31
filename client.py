# SEND DATA
import socket     
import time          
s = socket.socket()        
port = 12345               
s.connect(('172.31.150.22', port))
x = 0
sup ='ok'
com = ['testcom1','testcom2','testcom3','4']
def sendcomgoto(datast):
    input_string = datast.encode()
    s.sendall(input_string)
try:
    while x<3:
        sendcomgoto(com[x])
        x = x+1
except:
    print("loop while error occur")

s.close()
