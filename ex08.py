from selenium import webdriver
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("headless") #구글 브라우저를 띄우지 않고 크롤링#
options.add_argument("window-size=1920x1080")
options.headless = True

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url='https://www.google.com/search?q=%EC%86%A1%EC%A4%91%EA%B8%B0&tbm=isch&ved=2ahUKEwiUoqqHqvWCAxUug68BHW0MDHUQ2-cCegQIABAA&oq=%EC%86%A1%EC%A4%91%EA%B8%B0&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgARQAFgAYO8IaABwAHgAgAFZiAFZkgEBMZgBAKoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=FIltZZTIFK6Gvr0P7ZiwqAc&bih=963&biw=1920'
browser.get(url)

#이전 스크롤 높이
prev_height=browser.execute_script('return document.body.scrollHeight')
print("이전높이", prev_height)

while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    curr_height=browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
        break
    prev_height = curr_height
    
res=browser.page_source

time.sleep(1)

def fn_soup(res):
    soup = BeautifulSoup(res, "lxml")
    images = soup.find_all('div', attrs={'class':'isv-r PNCib ViTmJb BUooTd'})
    for idx, image in enumerate(images):
        title=image.find('div', attrs={'class': 'zbRPDe M2qv4b P4HtKe'}).get_text()
        print(idx + 1, title)

fn_soup(res)

