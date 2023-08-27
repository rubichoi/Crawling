
## 내 개인 노트북 방화벽 오류로 실행안됨

import urllib.request
import urllib.parse
import sys
import io

API = "https://api.ipify.org"

values = {
    'format': 'json'
}
print('before',values)
params = urllib.parse.urlencode(values)
print('after',params)
#요청 URL 생성
url = API + "?" + params
print("요청 url=", url)
#읽기
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)


