import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# prompt user for URL input
url = input("Enter URL: ")

# set to keep track of visited URLs
visited = set()

# list to store image links
img_links = set()

# function to scrape images from a URL and its linked pages
def scrape_images(url):
    global visited
    global img_links
    # add URL to visited set
    visited.add(url)
    
    # send GET request to URL and parse HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # extract image links from homepage
    img_tags = soup.find_all("img")
    img_links.update(img.get("src") or img.get("data-src") or img.get("data-original") or img.get("data-img") or img.get("data-image") for img in img_tags)
    # find all links on page and extract their URLs
    links = soup.find_all("a")
    link_urls = [link.get("href") for link in links]

    # extract image links from each linked page with the same domain
    for link_url in link_urls:
        # handle relative links by joining with base URL
        full_link_url = urljoin(url, link_url)
        if full_link_url not in visited:
            try:
                # check if link URL has the same domain as input URL
                if urlparse(full_link_url).netloc == urlparse(url).netloc:
                    print("Scraping image links from " + link_url)
                    # scrape images from linked page recursively
                    scrape_images(full_link_url)
            except Exception as e:
                print("Couldnt scrape from "+ link_url + " due to " + str(e))
                # handle any errors that may occur (e.g. invalid links)
                continue

# scrape images from homepage and linked pages with the same domain
scrape_images(url)
print(img_links)
# write image links to file
with open("image_links.txt", "w") as f:
    for link in img_links:
        f.write(str(link) + "\n")
