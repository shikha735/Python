# python web crawler to get titles of problems in five pages from 'www.geeksforgeeks.org' and store it in a text file.

import requests
from bs4 import BeautifulSoup


def geek_spider(max_pages):
    page = 1
    fw = open('geeks.txt', 'w')
    while page <= max_pages:
        url = 'http://www.geeksforgeeks.org/page/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        fw.write("Page " + str(page) + '\n')
        for link in soup.findAll('a', {'rel': 'bookmark'}):
            title = link.text
            fw.write(title + '\n')
        page += 1
    fw.close()
geek_spider(5)
