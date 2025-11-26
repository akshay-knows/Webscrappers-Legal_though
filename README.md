                              🧠 XKCD WEB SCRAPER
                                      |
        ------------------------------------------------------------------
        |                           |                                   |
   🛠 Imports                 🗂 Folder Setup                      🏁 Initial Setup
        |                           |                                   |
   - bs4 → BeautifulSoup       - os.makedirs("comics")          - url = "https://xkcd.com/1"
   - requests → rq             - exist_ok=True                  - base_url ="https://xkcd.com/"
   - os                                                            - print welcome message
                                                                   - input() prompt
        |
        |
        --------------------------- 🌀 MAIN LOOP ----------------------------
                                      while "#" not in url
        |
        |--------------- PART 1: REQUEST PAGE ------------------
        |          - rq.get(url)
        |          - response.content
        |
        |--------------- PART 2: PARSE HTML --------------------
        |          - soup = BeautifulSoup(response)
        |          - Find comic image:
        |               soup.select("#comic img")[0]
        |          - Extract src:
        |               img_src = element["src"]
        |
        |--------------- PART 3: DOWNLOAD IMAGE ----------------
        |          - Extract filename:
        |               img_name = img_src.split("/")[-1]
        |          - Build full URL:
        |               img_url = "http:" + img_src
        |          - rq.get(img_url)
        |          - Save file:
        |               open("comics/"+img_name, "wb")
        |          - print("Image Downloaded")
        |
        |--------------- PART 4: GO TO NEXT PAGE ---------------
        |          - Find next button:
        |               soup.select(".comicNav a[rel='next']")[0]
        |          - Extract href:
        |               next_href = next_a["href"]
        |          - Build next URL:
        |               url = base_url + next_href
        |          - print next URL
        |
        ------------------------ LOOP REPEATS -------------------------
