from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os


opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("라이언")
url = base + quote

res = req.urlopen(url)
savePath = "C:/Users/user/python_create_app_1-master/ImageDown/"  

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select(".photo_tile._grid .tile_item._item .thumb")

for i, img_list in enumerate(img_list, 1):
    print(img_list['data-source'])
    # fullFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
    # req.urlretrieve(img_list['data-source'], fullFileName)

print("다운로드 완료")
