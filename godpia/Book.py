import bs4

class Chapter:
    # status는 nothing, selected, selected_by_others, completed
    def __init__(self, shortened_chapter_name:str, no:int, data_user_id:str, css_class:str):
        self.no = no
        self.shortened_chapter_name = shortened_chapter_name
        self.css_class = css_class
        self.data_user_id = data_user_id
        self.set_status()

    def set_status(self):
        if not self.css_class:
            # False라는 것은 user가 나라는 것
            self.status = 'NOTHING' #'비어있는 것'
        elif self.css_class[0] == 'spot1':
            self.status = 'FINISHED_BY_ME' #'내가 친 것'
        elif self.css_class[0] == 'spot2':
            self.status = 'RESERVED_BY_ME' #'내가 예약한 것'
        elif self.css_class[0] == 'spot3':
            self.status = 'RESERVED_BY_OTHER' #'남이 예약한 것'
        elif self.css_class[0] == 'spot4':
            self.status = 'FINISHED_BY_OTHER' #'남이 친 것'
        else:
            print(f"{self.shortened_chapter_name} {self.no} Chapter status를 정할 수 없습니다. css_class:{self.css_class}")
            self.status = ''


class Book:
    def __init__(self, name, ul:bs4.element.Tag):
        self.name = name
        self.shortened_book_name = ''
        self.chapters = []
        self.status = '' # 이 책이 쓸게 남아있는 상태인지 IN_PROGRESS, FINISHED
        self.parse(ul)
        self.set_status()

    def parse(self, ul):
        # user_id와 li의 class를 이용해 status판단 가능
        lis = ul.find_all("li")
        for li in lis:
            c = Chapter(li['datavol'], int(li.text), li['datauserid'], li['class'])
            self.chapters.append(c)
        self.shortened_book_name = lis[0]['datavol']

    def set_status(self):
        # chapters가 모두 끝났다면 'FINISHED'
        finished_cnt = 0
        reserved_by_me = 0
        reserved_by_other = 0
        for chapter in self.chapters:
            if chapter.status == 'FINISHED_BY_ME' or chapter.status == 'FINISHED_BY_OTHER':
                finished_cnt += 1
            elif chapter.status == 'RESERVED_BY_ME':
                reserved_by_me += 1
            elif chapter.status == 'RESERVED_BY_OTHER':
                reserved_by_other += 1
        if finished_cnt == len(self.chapters):
            self.status = 'FINISHED'
        elif reserved_by_me > 0 and reserved_by_other == 0:
            self.status = 'INPROGRESS_BY_ME'
        elif reserved_by_me == 0 and reserved_by_other > 0:
            self.status = 'INPROGRESS_BY_OTHER'
        elif reserved_by_me == 0 and reserved_by_other == 0:
            self.status = 'READY'
        else:
            print(f'Book의 상태를 결정할 수 없습니다. reserved_by_me:{reserved_by_me} reserved_by_other:{reserved_by_other}')

    def isFinished(self):
        return self.status == 'FINISHED'