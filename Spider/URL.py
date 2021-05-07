import urllib.request
response = urllib.request.urlopen(
    'https://www.qcc.com/web/search?key=%E7%99%BE%E5%BA%A6')
html = response.read()
print(html)
int
