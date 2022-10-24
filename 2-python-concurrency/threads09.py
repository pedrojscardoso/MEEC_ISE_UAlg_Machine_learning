""" count the chars in a list of web pages"""  # SEQUENCIAL VERSION
import urllib.request, time, threading
from queue import Queue
from urls import url_list  # url_list - tuple of urls

chars_total = 0  # chars counter


def get_page_size(url):  # sum the chars of each page
    global chars_total
    try:
        with urllib.request.urlopen(url) as response:
            chars_total += len(response.read())
    except:
        print('error reading {}'.format(url))


s = time.time()
for url in url_list:
    get_page_size(url)
print('took {} seconds'.format(time.time() - s))