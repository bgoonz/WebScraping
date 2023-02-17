import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://bgoonz-blog.netlify.app/blog/"

# Make a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the image tags in the HTML
image_tags = soup.find_all("img")

# Loop through all the image tags and check if each image is missing
for image_tag in image_tags:
    src = image_tag.get("src")
    if src is None or src == "":
        print(f"Missing image found in {url}")
    else:
        response = requests.get(src)
        if response.status_code != 200:
            print(f"Missing image found at {src} in {url}")
