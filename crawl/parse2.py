#
from bs4 import BeautifulSoup
text = open("page2.html").read()

bsobj = BeautifulSoup(text)

div_price = bsobj.find("div", {"class":"price"})
print(div_price.text)