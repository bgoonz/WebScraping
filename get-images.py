from bs4 import BeautifulSoup
import requests


def get_links(url):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    links = []
    for link in soup.find_all('img'):
        link_url = link.get('src')

        if link_url is not None and link_url.startswith('https'):
            links.append(link_url + '\n')

    write_to_file(links)
    return links


def write_to_file(links):
    with open('data.txt', 'a') as f:
        f.writelines(links)


def get_all_links(url):
    for link in get_links(url):
        get_all_links(link)


r = 'https://bgoonz-blog.netlify.app/'
write_to_file([r])
get_all_links(r)

# 
# from bs4 import BeautifulSoup
# import requests
# 
# def get_links(urls):
#     links = []
#     for url in urls:
#         response = requests.get(url)
#         data = response.text
#         soup = BeautifulSoup(data, 'html.parser')
#         for link in soup.find_all('img'):
#             link_url = link.get('src')
#             if link_url is not None and link_url.startswith('https'):
#                 links.append(link_url + '\n')
#         write_to_file(url, links)
# 
# def write_to_file(url, links):
#     with open('siteData.txt', 'a') as f:
#         f.writelines("From " + url+ ":\n")
#         f.writelines(links)
# 
# def get_all_links(urls):
#     for currentUrl in urls:
#         get_links(currentUrl)
# 
# r = [ 'https://bgoonz-blog.netlify.app/']
# 
# write_to_file([r])
# 
# 
# get_links(r)
