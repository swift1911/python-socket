import socket
try:
    socket.getaddrinfo("www.baidu.com", 80, 0, 0, socket.IPPROTO_TCP)
    [(2, 1, 6, '', ('82.94.164.162', 80)),
     (10, 1, 6, '', ('2001:888:2000:d::a2', 80, 0, 0))]
    socket.sendto("hello",'127.0.0.1')
except:
    print 'error'
str=socket.gethostname()
print(str)
