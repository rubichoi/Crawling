import sys
import io
import urllib.request as dw

htmlURL ="http://www.naver.com"

imgUrl1 = 'https://ssl.pstatic.net/melona/libs/1459/1459881/0185dfddd6603c7932f3_20230823135454197.jpg'
imgUrl2 = 'https://naverpa-phinf.pstatic.net/MjAyMzA4MjRfMTM5/MDAxNjkyODQ2OTE5MTk3.zJWqewhpY7zrbBGtG-2bzy2m0MuK01LQypdsgxbyCIkg.IxAmRCNMntqFWkp3VFt0KKOl_wBDulS_Pqp14Un4GEkg.JPEG/PC_05_16928469191848763639684920370367.jpg'


savePath1 ="C:/Users/user/python_create_app_1-master/main1.jpg"
savePath2 ="C:/Users/user/python_create_app_1-master/main2.jpg"

dw.urlretrieve(imgUrl1, savePath1)
dw.urlretrieve(imgUrl2, savePath2)

print("다운로드 완료!")