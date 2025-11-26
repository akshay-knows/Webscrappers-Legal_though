from bs4 import BeautifulSoup as bs
import requests as rq
import os

os.system("cls")

url = "https://mausam.imd.gov.in/imd_latest/contents/satellite.php"
response = rq.get(url)

soup = bs(response.content,"html.parser")
img_element = soup.select("#images img")[0]
img_src = img_element['src']

base = "https://mausam.imd.gov.in/"

img_url = base + img_src.replace("../../","")

response = rq.get(img_url)

file_name = img_src.split("/")[-1]
print("--Image Downloading☄️--")
with open(file_name,"wb") as f:
    f.write(response.content)
