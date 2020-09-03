from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_755665.html"#input('Enter - ')
html = urlopen(url, context= ctx).read()
soup = BeautifulSoup(html, "html.parser")
all_span = soup.findAll('span')
total = 0
for span in all_span:
    #print(int(span.text))
    total+=int(span.text)
print("Total is ",total)
