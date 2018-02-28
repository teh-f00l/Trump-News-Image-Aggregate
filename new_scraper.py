import bs4 as BeautifulSoup
import os
import urllib
import urllib.request

#https://www.nytimes.com

endpt=urllib.request.urlopen('https://www.nytimes.com').read()
site=BeautifulSoup.BeautifulSoup(endpt,'lxml')

counter=0
links=list()
for url in site.find_all('a'):
    if 'https' in url.get('href') and 'trump' in url.get('href') :
        links.append(url.get('href'))
        counter+=1
        # print(url.get('href'))
#print((links))
# for i in links:
#     if 'Trump' not in i:
#         links.remove(i)
# links.remove(links[1])
# links.remove(links[0])
# print(len(links))
# for link in links:
#     print(link)
# templink=urllib.request.urlopen(links[6]).read()
# a=BeautifulSoup.BeautifulSoup(templink,'lxml')
# print(a)
imgLinks=list()
for i in links:
    templink=urllib.request.urlopen(i).read()
    a=BeautifulSoup.BeautifulSoup(templink,'lxml')
    for image in a.find_all('img'):
        imgLinks.append(image.get('src'))
        print(image.get('src'))
for img in imgLinks:
    if 'https' in img:
        counter+=1
        urllib.request.urlretrieve(img,'dTrump_img'+str(counter)+'.jpg')
        #urllib.request.urlretrieve(imgUrl, os.path.basename(imgUrl`))
