
from bs4 import BeautifulSoup as bs
import requests as rq
import os
os.system("cls")

print("Hi from 'xkcd.com'\n\n※ This is an open source webscrapping project.\n\n※ Images will be saved in comics folder.\nPS: No robots.txt harmed !!")
input("\nPress Any Key to continue")
url = "https://xkcd.com/1"
base_url = "https://xkcd.com/"

# making folder

os.makedirs("comics", exist_ok=True)
print(f"Redirecting to {base_url}")


while "#" not in url:
    #part1-requesting webpage
    response = rq.get(url)

    #parsing 
    soup = bs(response.content,"html.parser")

    #part2 - img url
    img_element = soup.select("#comic img")[0] # CSS Selector
    img_src = img_element["src"] # dictionary

    #get file name 
    img_name = img_src.split("/")[-1] 

    # part3 - Downloading img
    img_url = "http:" + str(img_src) #str only used for in case of error !
    response = rq.get(img_url)
    with open("comics/" + img_name,"wb") as f:
        f.write(response.content)
        print("Image Downloaded ✅")

    # part 4 - going to next page
    next_a = soup.select(".comicNav a[rel='next']")[0] #css selector
    next_href = next_a["href"] #next page
    url = base_url + next_href
    print("Next Url ↪-- ",url)
  
