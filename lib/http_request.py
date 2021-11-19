import requests

class HttpRequest:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

    def get(self, url):
      session = requests.Session()
      return session.get(url, headers=self.headers)
