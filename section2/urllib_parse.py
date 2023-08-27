import urllib.request
from urllib.parse import urlparse
import sys
import io


url = "http://www.encar.com/"

mem = urllib.request.urlopen(url)

print(type(mem))
print("geturl :",mem.geturl())
print("status :",mem.status) # 200(정상) 404(요청한페이지없음), 403(거절), 500(서버 에러)
print("headers :",mem.getheaders())
print("info :",mem.info(),"\n")
print("getcode :",mem.getcode())
print("read :",mem.read(30).decode('utf-8')) # euc-kr
print(urlparse('http://www.encar.co.kr?test=test'))
print(urlparse('http://www.encar.co.kr?test=test').query)
