#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install google_images_download


# In[5]:


from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.naver.com/')
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("새파일.txt", 'w')
for anchor in soup.select("span.ah_k"):
    data = str(i) + "위 : " + anchor.get_text() + "\n"
    i = i + 1
    f.write(data)
f.close()


# In[6]:


from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"워너원 강다니엘, 엑소 백현, 박보검, 송중기, 워너원 황민현, 엑소 시우민, 강동원, 이종석, 이준기, 마동석, 조진웅, 조세호, 안재홍, 윤두준, 이민기, 김우빈, 육성재, 공유, 방탄소년단 정국, 아이콘 바비, 워너원 박지훈, 엑소 수호 ","limit":50,"print_urls":True, "format": "jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images


# In[3]:


from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images

