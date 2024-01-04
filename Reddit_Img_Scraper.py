from bs4 import *
import requests
import os
from PIL import Image
import io
import random
import datetime


def download_images(images, numImgs=2):
    usedLinks = []
    if len(images) != 0:
        for i,image in enumerate(images):
          if i == 0:
                continue
          if numImgs == 1:
            image_link = image["src"]
          else:
            image_link = image["href"]
    
          if "https://preview.redd.it/" not in image_link or image_link in usedLinks:
              continue

          print(image_link)
          r = requests.get(image_link).content
            #try:

                # possibility of decode
                #r = str(r, 'utf-8')

          #  except UnicodeDecodeError:

          imageStream = io.BytesIO(r)
          imageFile = Image.open(imageStream)
      
          # Save the image
          try:
            imageFile.save("C:\\Users\\tranb\\Pictures\\pics\\"+str(random.randint(10**12,10**18)+1)+".png")
          except:
            imageFile.convert('RGB').save("C:\\Users\\tranb\\Pictures\\pics\\"+str(random.randint(10**12,10**18)+1)+".png")
          usedLinks.append(image_link)
    print("All Images Downloaded at " + str(datetime.datetime.now()))


def main(url,numImgs=2):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    if numImgs ==1:
      images = soup.findAll('img')
    else:
      images = soup.findAll('a')
    download_images(images, numImgs)

url = ""
main(url)