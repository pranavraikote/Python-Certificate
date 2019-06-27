from PIL import Image, ImageDraw, ImageFont
import time
import os

#IF reading set of names from a file
#f = open('New Text document.txt','r')
#names = f.read().splitlines()

names=['Put in names here in a list']

#a=os.getcwd()
#folder_name = '6th Sem'
#if not os.path.exists(folder_name):
#    os.mkdir(folder_name)
#    a=a+'\\'+folder_name
#    os.chdir(a)


for i in names:    

    image = Image.open('Certificate.png')

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Ubuntu-Regular.ttf', size=32)

    (x,y) = (390,329)

    message = i

    color = 'rgb(0,0,0)'

    draw.text((x,y), message, fill=color, font=font)

    message1 = 'II'

    (x1,y1) = (754,329)

    save = message+'.png'

    draw.text((x1,y1), message1, fill=color, font=font)

    image.save(save)


