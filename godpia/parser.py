from bs4 import BeautifulSoup
from Book import Book

# Book을 return함
m = {
    "구약": [],
    "신약": []
}


def parse(userId, page_string) -> list:
    # userId에 따라 return값이 달라짐
    soup = BeautifulSoup(page_string, 'html.parser')
    table1 = soup.find("div", {"class":"clsVolBody"}).find("table")
    trs = table1.find_all("tr")
    for tr in trs:
        book_name = tr.find('th').text
        b = Book(book_name, tr.find('ul'))

    return []

filename="구약_쓸장선택.html"
f = open(f'{filename}', 'r', encoding='utf-8').read()

parse("oceanfog", f)
