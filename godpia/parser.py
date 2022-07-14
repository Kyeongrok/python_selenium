from bs4 import BeautifulSoup
from Book import Book
import random

class Target:
    def __init__(self, sbn, chapters):
        self.sbn:str = sbn
        self.chapters = chapters


class TargetSelector:
    def __init__(self, page_string, rnd_page_from=3, rnd_page_end=5):
        self.books = []
        self.from_chapter_no = 1
        self.rnd_page_from = rnd_page_from
        self.rnd_page_end = rnd_page_end
        self.parse(page_string)

    def parse(self, page_string):
        soup = BeautifulSoup(page_string, 'html.parser')
        table1 = soup.find("div", {"class": "clsVolBody"}).find("table")
        self.trs = table1.find_all("tr")
        self.set_books()

    def get_target_book_chapters(self) -> Target:
        target_book:Book = ''
        rnd_int = random.randint(self.rnd_page_from, self.rnd_page_end)
        target_chapter_no = []
        for book in self.books:
            print(book.name, book.shortened_book_name, book.status)
            if book.status == 'INPROGRESS_BY_ME':
                target_book = book
                break
        if target_book == '':
            print('선택된 장이 없습니다. 장을 선택 해주세요.')

        idx = 0
        while rnd_int > 0 and idx < len(target_book.chapters):
            # print(target_book.chapters[idx].status, target_book.chapters[idx].no)
            if target_book.chapters[idx].status == 'RESERVED_BY_ME':
                target_chapter_no.append(target_book.chapters[idx].no)
                rnd_int -= 1
            idx += 1

        return Target(target_book.shortened_book_name, target_chapter_no)


    def set_books(self):
        for tr in self.trs:
            book_name = tr.find('th').text
            # print(tr)
            b = Book(book_name, tr.find('ul'))
            self.books.append(b)


if __name__ == "__main__":
    f = open(f'{"신약_쓸장선택.html"}', 'r', encoding='utf-8').read()
    f2 = open(f'{"신약_쓸장선택.html"}', 'r', encoding='utf-8').read()

    ts = TargetSelector(f)
    ts.parse(f2)
    target:Target = ts.get_target_book_chapters()

    print(target.sbn, target.fr, target.to)

