import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",8888))
data=s.recv(1024).decode()
print(data)
string="HELLO gupta.vis\n"
s.send(string.encode())
print(string)
while True:
  data=s.recv(1024).decode()
  print(data)
  x=data.split(' ',1)
  if (x[0]=="DONE"):
     s.close()
     break
  if (x[0]=="MATH"):
     answer=eval(x[1])
     m="ANSWER"+" "+str(int(answer))+"\n"
     s.send(m.encode())
     print(m)
