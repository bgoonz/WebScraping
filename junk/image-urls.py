import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = "https://bgoonz-blog.netlify.app/blog/"




# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the image tags on the website
image_tags = soup.find_all('img')

# Extract the src attribute of each image tag and store it in a list
image_urls = [img['src'] for img in image_tags]

# Print the list of image URLs
print(image_urls)
