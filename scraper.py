# Print the first found div on html page
import requests
from bs4 import BeautifulSoup
import io
from PIL import Image
import random
import moviepy as mpy

url=''
response = requests.get(url)
def download_images(images):
    if len(images) != 0:
        print("There are " + str(len(images)) + " images")
        for i,image in enumerate(images):
          if i == 0:
            continue

        try:
            image_link = image["src"]
        except:
            try:    
                image_link = image["data-srcset"]
            except:
                try:
                    
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:
                            pass
            
            r = requests.get(image_link).content
            #try:

                # possibility of decode
                #r = str(r, 'utf-8')

          #  except UnicodeDecodeError:
            imageStream = io.BytesIO(r)
            imageFile = Image.open(imageStream)

            # Resize the image

            # Save the resized image
            try:
              imageFile.save("C:\\Users\\tranb\\Pictures\\pics\\"+str(random.randint(10**11,10**12))+".png")
            except:
              imageFile.convert('RGB').save("C:\\Users\\tranb\\Pictures\\pics\\"+str(random.randint(10**11,10**12))+".png")



    print("All Images in Collection Downloaded!")
extensions = ['.jpg', '.jpeg', '.png']

def handleCollection(url):
    r = requests.get(url)
    if '404' in r.content:
        for ext in extensions:
            r = requests.get(url + ext)
            if '404' in r.content:
                continue
            else:
                break
    if ' ' in url:
            restOfStrArr = url.split(' ')
            for substr in restOfStrArr:
                url += substr
    print(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img')
    download_images(images)

domains = ['catbox.moe/', 'imgbox.com/', 'imgchest.com/','imgur.com/', 'imgur.com/a/', 'imgur.com/gallery/', 'imgur.com/r/', 'imgur.com/t/', 'imgur.com/user/', 'imgur.com/album/', 'imgur.com/gallery/', 'imgur.com/a/', 'imgur.com/r/', 'imgur.com/t/', 'imgur.com/user/', 'imgur.com/album/', 'imgur.com/gallery/', 'imgur.com/a/', 'imgur.com/r/', 'imgur.com/t/', 'imgur.com/user/', 'imgur.com/album/', 'imgur.com/gallery/', 'imgur.com/a/', 'imgur.com/r/', 'imgur.com/t/', 'imgur.com/user/', 'imgur.com/album/', 'imgur.com/gallery/', 'imgur.com/a/', 'imgur.com/r/', 'imgur.com/t/', 'imgur.com/user/', 'imgur.com/album/', 'imgur.com/gallery/', 'imgur.com/a/', 'imgur.com/r/', 'imgur.com/t/', 'imgur.com/user/', 'imgur.com/album/', 'imgur.com/gallery/', 'imgur.com/a/', 'imgur.com/r/', 'imgur.com/t/', 'imgur.com/user/', 'imgur.com/album/', 'imgur.com/gallery/', 'imgur.com/a/', 'imgur.com/r/', 'imgur.com/t/', 'imgur.com/user/', 'imgur.com/album/', 'imgur.com/gallery/', 'imgur.com/a/', 'imgur.com/r/', 'imgur.com/t/', 'imgur.com/user/', 'imgur.com/album/', 'imgur.com/gallery/']
for domain in domains:
    respTxt = response.text
    while respTxt.find(domain) != -1:
        if respTxt[respTxt.find('catbox.moe'):respTxt.find('catbox.moe')+len('catbox.moe/c/')] == "catbox.moe/c/":
            handleCollection('https://'+respTxt[respTxt.find('catbox'):].split('<')[0])
        ind = respTxt.find(domain)
        restOfStr = ''
        for char in respTxt[ind+len(domain):]:
            if char == '.' or char == '<':
                break
            restOfStr += char

        if ' ' in restOfStr:
            restOfStrArr = restOfStr.split(' ')
            restOfStr = ''
            for substr in restOfStrArr:
                restOfStr += substr
        print(domain + restOfStr)
        if 'catbox' in domain and '/c/' not in restOfStr:
            for ext in extensions:
                    r = requests.get('https://files.catbox.moe/' + restOfStr + ext).content
                    if '404' in r:
                        r = requests.get('https://litter.catbox.moe/' + restOfStr + ext).content
                        if '404' in r:
                            continue
                        else:
                            break
                    else:
                        break
        else:
            print('New domain: ' + domain + restOfStr)
            handleCollection('https://' + domain + restOfStr)
                            
        # Save the image
        imageStream = io.BytesIO(r)
        imageFile = Image.open(imageStream)
        imageFile.save('C:\\Users\\tranb\\Pictures\\pics\\'+str(random.randint(10**10,10**12))+".png")
        respTxt = respTxt[ind+len(domain):]