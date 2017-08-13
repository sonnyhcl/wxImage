
# coding: utf-8

# In[ ]:


import os
import math
import itchat
import PIL.Image as Image
import platform

if platform.system() == 'Linux':
    enableCmdQR = True
else:
    enableCmdQR = False

itchat.auto_login(enableCmdQR=enableCmdQR, hotReload=True)

friends = itchat.get_friends(update=True)
username = friends[0]["UserName"]
if not os.path.exists(username):
    os.mkdir(username)
    for i, friend in enumerate(friends):
        with open(username + "/" + str(i) + ".png", 'wb') as fileImage:
            fileImage.write(itchat.get_head_img(userName=friend["UserName"]))

print("itchat login done...")


# In[ ]:

pics = os.listdir(username)
numPic = len(pics)

eachsize = int(math.sqrt(float(640 * 640) / numPic))

numline = int(640 / eachsize)
toImage = Image.new('RGB', (int(numline * eachsize), int(numPic / numline * eachsize)))


# In[ ]:

for i, pic in enumerate(pics):
    try:
        img = Image.open(username + "/" + pic)
    except IOError:
        print("IOError: can not read %d.png" % i)
    else:
        img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
        x = int(i % numline)
        y = int(i / numline)
        toImage.paste(img, (x * eachsize, y * eachsize))

toImage.save(username + ".png")


# In[ ]:

itchat.send_image(username + ".png", 'filehelper')

