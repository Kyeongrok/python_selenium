from bs4 import BeautifulSoup
from Book import Book

def parse(page_string) -> list:
    # userId에 따라 return값이 달라짐
    soup = BeautifulSoup(page_string, 'html.parser')
    table1 = soup.find("div", {"class":"clsVolBody"}).find("table")
    trs = table1.find_all("tr")
    books = []
    for tr in trs:
        book_name = tr.find('th').text
        # print(tr)
        b = Book(book_name, tr.find('ul'))
        books.append(b)
        print(b.name, b.status)
        # 끝난게 아닌 책 중에 내가 예약한 장이 있는 책

    return books

f = open(f'{"신약_쓸장선택.html"}', 'r', encoding='utf-8').read()
f2 = open(f'{"신약_쓸장선택.html"}', 'r', encoding='utf-8').read()

# Book을 return함
m = {
    "구약": [],
    "신약": []
}

m['구약'] = parse(f)
m['신약'] = parse(f2)
print(m)
