#
from bs4 import BeautifulSoup
text = open("page1.html").read()

bsobj = BeautifulSoup(text)

h1 = bsobj.find("h1")
print(h1.text)