import requests
from bs4 import BeautifulSoup

url='https://www.google.com/search?q=%EC%86%A1%EC%A4%91%EA%B8%B0&tbm=isch&ved=2ahUKEwiUoqqHqvWCAxUug68BHW0MDHUQ2-cCegQIABAA&oq=%EC%86%A1%EC%A4%91%EA%B8%B0&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgARQAFgAYO8IaABwAHgAgAFZiAFZkgEBMZgBAKoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=FIltZZTIFK6Gvr0P7ZiwqAc&bih=963&biw=1920'
header={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
images = soup.find_all('div', attrs={'class':'isv-r PNCib ViTmJb BUooTd'})
for idx, image in enumerate(images):
    title=image.find('div', attrs={'class': 'zbRPDe M2qv4b P4HtKe'}).get_text()
    print(idx + 1, title)