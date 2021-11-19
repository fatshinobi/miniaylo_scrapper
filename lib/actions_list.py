#from bs4 import BeautifulSoup
#import time
#import pdb

#from lib.http_request import HttpRequest
#from lib.book import Book

#class ActionsList:
#    def __init__(self, page_url):
#        request = HttpRequest()
#        req = request.get(page_url)

#        bs = BeautifulSoup(req.text, 'html.parser')

#        actions_list = bs.find_all('tr', {'class':'added'})

#        pdb.set_trace()
