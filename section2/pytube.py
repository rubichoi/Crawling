import os
import subprocess

import pytube


yt = pytube.YouTube("https://youtu.be/3kGAlp_PNUg?si=SBkkJ7LxAyp4EnGP") 

vids= yt.streams.all()

#
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("다운받을 화질은? (0 ~ 21 입력)"))

parent_dir = "C:/Users/user/python_create_app_1-master"
vids[vnum].download(parent_dir) #

new_filename = input("mp3 file name?")

oriFileName = vids[vnum].default_filename 


subprocess.call(['ffmpeg', '-i',                 # cmd 
    os.path.join(parent_dir, oriFileName),
    os.path.join(parent_dir, new_filename)
])

print('Downloaded video and coverted to mp3 !')
