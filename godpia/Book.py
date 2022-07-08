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
            print(self.css_class, self.data_user_id, '비어있는 것')
            pass
        elif self.css_class[0] == 'spot1':
            print(self.css_class, self.data_user_id, '내가 친 것')
            self.status = ''
        elif self.css_class[0] == 'spot2':
            print(self.css_class, self.data_user_id, '내가 예약한 것')
            self.status = ''
        elif self.css_class[0] == 'spot3':
            print(self.css_class, self.data_user_id, '남이 예약한 것')
            self.status = ''
        elif self.css_class[0] == 'spot4':
            print(self.css_class, self.data_user_id, '남이 친 것')
            self.status = ''
        else:
            print("Chapter status를 정할 수 없습니다.")
            self.status = ''



class Book:
    def __init__(self, name, tr:bs4.element.Tag):
        self.name = name
        self.chapters = []
        self.status = '' # 이 책이 쓸게 남아있는 상태인지 IN_PROGRESS, FINISHED

    def parse(self, ul):
        # user_id와 li의 class를 이용해 status판단 가능
        lis = ul.find_all("li")
        for li in lis:
            c = Chapter(li['datavol'], int(li.text), li['datauserid'], li['class'])
            self.chapters.append(c)

    def set_status(self):
        # chapters가 모두 끝났다면 'FINISHED'
        self.status = ''

    def isFinished(self):
        return self.status == 'FINISHED'




