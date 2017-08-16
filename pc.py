from selenium import webdriver
from bs4 import BeautifulSoup
import requests


picksrclist = []

def picklist(pic_src):
    global picksrclist
    picksrclist.append(pic_src)

def save_img():
    for img in picksrclist:
        imgfile = requests.get(img)
        img_src = str(img)
        filenamestar = img_src.index('.com/') + 5
        filenameend = img_src.index('?')
        filename = img_src[filenamestar:filenameend] + '.jpg'
        f = open(filename,'ab')
        f.write(imgfile.content)
        f.close()

#r = requests.get('https://unsplash.com')
#print(r.text)

web_url = 'https://unsplash.com'
driver = webdriver.PhantomJS()
driver.get(web_url)
driver.set_page_load_timeout(200)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

print('开始获取A标签......')

all_pic = BeautifulSoup(driver.page_source,'lxml').find_all('a','ODWzM')


for a in all_pic:
    pic_src = str(a)
    ind = pic_src.index('src=\"')
    sta = ind+5
    endind = pic_src.index('\"/>')
    pic_src = pic_src[sta:endind]
    #print(str(ind),pic_src)
    picklist(pic_src)

picksrclist = {}.fromkeys(picksrclist).keys()

#for i in picksrclist:
#    print(i)

save_img()


