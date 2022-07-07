import bs4

class Chapter:
    # status는 nothing, selected, selected_by_others, completed
    def __init__(self, no):
        self.no = ''
        self.status = ''

class Book:
    def __init__(self, name, tr:bs4.element.Tag):
        self.name = name
        self.chapters = []
        self.status = '' # 이 책이 쓸게 남아있는 상태인지 IN_PROGRESS, FINISHED
        r = self.parse(tr)

    def parse(self, ul):
        # user_id와 li의 class를 이용해 status판단 가능
        lis = ul.find_all("li")
        for li in lis:
            print(li.text, li['class'], li['datauserid'], li['datavol'])
        return []

    def isFinished(self):
        return self.status == 'FINISHED'




