# XKCD Comic Scraper (Python)

A lightweight script that downloads the entire XKCD archive by visiting each comic page, extracting the comic image, and saving it locally.

How it works
- Starts at the very first XKCD comic and iterates forward using the page's "Next" link.
- Fetches each comic page with HTTP requests.
- Parses HTML with BeautifulSoup to locate the #comic element and extract the image URL.
- Normalizes/builds the full image URL and downloads the image file.
- Creates a local comics/ folder in the current directory.
- Repeats until no next comic is found.

Key points
- Requires: Python, requests, beautifulsoup4.
- Output: images saved in comics/ for offline viewing.

