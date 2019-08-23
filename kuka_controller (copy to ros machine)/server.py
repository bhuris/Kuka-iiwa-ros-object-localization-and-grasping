# RECIEVE DATA
import socket               
 
# next create a socket object
s = socket.socket()         
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)     
print ("socket is listening" )          
c, addr = s.accept()     
print ('Got connection from', addr)
noofrecv = 0
print('after this data')
while noofrecv<5:    
  data=c.recv(1024).decode()
  print(data)
  print('dance dance\n')
  if data == 'bye' :break
  noofrecv +=1
c.close()
