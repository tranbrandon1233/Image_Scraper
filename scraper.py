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
            new_size = (1024, 1024)
            resized_image = imageFile.resize(new_size)

            # Save the resized image
            try:
              resized_image.save("C:\\Users\\tranb\\Pictures\\pics\\"+str(random.randint(10**11,10**12))+".png")
            except:
              resized_image.convert('RGB').save("C:\\Users\\tranb\\Pictures\\pics\\"+str(random.randint(10**11,10**12))+".png")



    print("All Images in Collection Downloaded!")
    
def handleCollection(url):
    r = requests.get(url)
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
        count = 0
        for char in respTxt[ind+len(domain):]:
            if char == '.' and domain =="catbox.moe/":
                break
            elif char == '<' and domain != "catbox.moe/":
                break
            restOfStr += char
            count += 1
        print('https://' + domain + restOfStr)
        try:
            r = requests.get('https://files.catbox.moe/' + restOfStr + '.png').content
            # Resize the image
            new_size = (1024, 1024)
            imageStream = io.BytesIO(r)
            imageFile = Image.open(imageStream)
            resized_image = imageFile.resize(new_size)

            # Save the resized image
            resized_image.save('C:\\Users\\tranb\\Pictures\\pics\\'+str(random.randint(10**11,10**12))+".png")
        except:
            try:
                r = requests.get('https://files.catbox.moe/' + restOfStr + '.jpg').content
                    # Resize the image
                new_size = (1024, 1024)
                imageStream = io.BytesIO(r)
                imageFile = Image.open(imageStream)
                resized_image = imageFile.resize(new_size)
                resized_image.save('C:\\Users\\tranb\\Pictures\\pics\\'+str(random.randint(10**11,10**12))+".jpg")
            except: 
                try:
                    r = requests.get('https://files.catbox.moe/' + restOfStr + '.png').content
                        # Resize the image
                    new_size = (1024, 1024)
                    imageStream = io.BytesIO(r)
                    imageFile = Image.open(imageStream)
                    resized_image = imageFile.resize(new_size)
                    resized_image.save('C:\\Users\\tranb\\Pictures\\pics\\'+str(random.randint(10**11,10**12))+".png")
                except:
                    try:
                        r = requests.get('https://litter.catbox.moe/' + restOfStr + '.jpg').content
                            # Resize the image
                        new_size = (1024, 1024)
                        imageStream = io.BytesIO(r)
                        imageFile = Image.open(imageStream)
                        resized_image = imageFile.resize(new_size)
                        resized_image.save('C:\\Users\\tranb\\Pictures\\pics\\'+str(random.randint(10**11,10**12))+".jpg")
                    except:
                        try:
                            r = requests.get('https://files.catbox.moe/' + restOfStr + '.jpeg').content
                                # Resize the image
                            new_size = (1024, 1024)
                            imageStream = io.BytesIO(r)
                            imageFile = Image.open(imageStream)
                            resized_image = imageFile.resize(new_size)
                            resized_image.save('C:\\Users\\tranb\\Pictures\\pics\\'+str(random.randint(10**11,10**12))+".png")
                        except:
                            try:
                                r = requests.get('https://litter.catbox.moe/' + restOfStr + '.jpeg').content
                                    # Resize the image
                                new_size = (1024, 1024)
                                imageStream = io.BytesIO(r)
                                imageFile = Image.open(imageStream)
                                resized_image = imageFile.resize(new_size)
                                resized_image.save('C:\\Users\\tranb\\Pictures\\pics\\'+str(random.randint(10**11,10**12))+".jpg")
                       
                            except:
                                print('https://' + domain + restOfStr)
                                handleCollection('https://' + domain + restOfStr)
                            
    

        # Save the resized image
        respTxt = respTxt[ind+1:]


    