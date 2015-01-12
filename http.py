import httplib
try:
    conn = httplib.HTTPConnection("www.baidu.com")
    conn.request("GET", "/index.html")  
    r1 = conn.getresponse()
    print r1.status, r1.reason
except:
    print r1.status,r1.reason
