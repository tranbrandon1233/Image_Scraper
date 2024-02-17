# Print the first found div on html page
import requests
from bs4 import BeautifulSoup
import io
from PIL import Image
import random
import urllib.request


#url=''
#response = requests.get(url)
def download_images(images,url=""):
    if len(images) != 0:
        print("There are " + str(len(images)) + " images")
        if(len(url)> 0):
                r = requests.get(url+'#gallery-1')
                soup = BeautifulSoup(r.text, 'html.parser')
                for link in soup.findAll('a'):
                    try:
                        print(link.get('href'))
                        imageStream = urllib.request.urlretrieve(link.get('href'), "C:\\Users\\tranb\\Pictures\\pics\\"+str(random.randint(10**11,10**12))+".png") 
                    except:
                        continue
        else:
            for img in images:
                try:
                    img_url = img['src']
                    if 'http' not in img_url:
                        img_url = '{}{}'.format(url, img_url)
                    #print(img_url)
                    randNum = str(random.randint(10**11,10**12))
                    imageStream = urllib.request.urlretrieve(img_url, "C:\\Users\\tranb\\Pictures\\test\\"+str(randNum)+".png") 
                    imageFile = Image.open(imageStream)
                    imageFile.save("C:\\Users\\tranb\\Pictures\\test\\"+str(randNum)+".png")
                except:
                    continue

    print("All Images in Collection Downloaded!")


extensions = ['.jpg', '.jpeg', '.png', '.webm']

def handleCollection(url):
    r = requests.get(url)
    if '404' in str(r.content):
        for ext in extensions:
            r = requests.get(url + ext)
            if '404' in str(r.content):
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
    download_images(images,url)
    
handleCollection('https://catbox.moe/c/ktlqk8')


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
        respTxt = respTxt[ind+len(domain):]
        if 'catbox' in domain and '/c/' not in restOfStr:
            for ext in extensions:
                    r = requests.get('https://files.catbox.moe/' + restOfStr + ext)
                    print('https://files.catbox.moe/' + restOfStr + ext)
                    if '404' in r.text:
                        if '404' in r.text:
                            continue
                        else:
                            r=r.content
                            break
                    else:
                        r=r.content
                        break
        else:
            print('New domain: ' + domain + restOfStr)
            handleCollection('https://' + domain + restOfStr)
                            
        # Save the image
        if '404' in str(r):
            continue
        elif 'webm' not in ext:
            imageStream = io.BytesIO(r)
            imageFile = Image.open(imageStream)
            imageFile.save('C:\\Users\\tranb\\Pictures\\pics\\'+str(random.randint(10**10,10**12))+".png")
        elif '404' not in r.text and 'webm' in ext:
            urllib.request.urlretrieve(url, 'C:\\Users\\tranb\\Pictures\\pics\\' + str(random.randint(10**12,10**18)+1) +'.webm')
            print("Video Downloaded")
