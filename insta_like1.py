from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

def get_url(id):
  url= 'https://www.instagram.com/{}'.format(id)
  return url

url = get_url('rla_thwjd')
driver=webdriver.Chrome('C:/info/chromedriver.exe')
driver.get(url)

time.sleep(2)

html = driver.page_source
soups=BeautifulSoup(html,'html.parser')
box=soups.select('.v1Nh3.kIKUG._bz0w')
hrefs=[]
for i in box:
    href=i.a['href']
    hrefs.append(href)
likes=[]
for i in range(0,len(hrefs)):
    url = get_url(hrefs[i])
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soups = BeautifulSoup(html, 'html.parser')
    like= soups.select('.sqdOP.yWX7d._8A5w5')
    if(len(like)==1):
        like_value=like[0].text
    else:
        like_num ='동영상'
    likes.append(like_value)

photo={}
like_nums=[]
for i in range(0,len(hrefs)):
    try:
        like_num=int(re.findall('\d+', likes[i])[0])
        #+(re.findall('\d+', likes[i])[1])
        like_nums.append(like_num)

    except IndexError:
        like_nums.append(0)
    photo[hrefs[i]] = like_nums[i]

like_ranks = sorted(photo.items(),
                              reverse=True,
                              key=lambda item: item[1])
for key, value in like_ranks:
    print(key, ":", value)

#for i in range(0,len(hrefs)):
    #    photo[hrefs[i]] = likes[i]
    #try:
    #   like_num=int(re.findall('\d+', likes[i])[0]+re.findall('\d+', likes[i])[1])
    #   like_nums.append(like_num)


    #except IndexError:
#   like_nums.append(0)


driver.close()
