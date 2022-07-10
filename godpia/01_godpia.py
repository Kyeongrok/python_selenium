from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import random, os

import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from godpia.Book import Book

class GodPiaBibleWriter:

    def __init__(self, mode):
        chromedriver_autoinstaller.install()

        if mode == 'login':
            id = os.environ.get("GODPIA_ID")  # 환경변수 설정
            password = os.environ.get("GODPIA_PASSWORD")  # 환경변수 설정
            if id == None or password == None:
                print('id또는 패스워드를 입력해주세요. 입력하는 방법은 READMD.md를 참고해주세요.')
                exit()
            driver = webdriver.Chrome(options=Options())
            self.login(driver, id, password)
            self.save_page("http://bible.godpia.com/write/sub020301.asp?cb_idx=2386#tb02-tab-tab", driver, "신약_쓸장선택.html")
        elif mode == 'debug':
            chrome_options = Options()
            chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
            driver = webdriver.Chrome(options=chrome_options)

        self.driver = driver


    def login(self, driver, id, password):
        url = 'http://www.godpia.com/login/login_page.asp?ishref=http://bible.godpia.com/frameindex.asp?url_flag=/index.asp?&ipserver=bible.godpia.com'
        driver.get(url)

        driver.find_element(By.ID, "inputID") \
            .send_keys(id)
        driver.find_element(By.ID, "inputPW") \
            .send_keys(password)

        xp = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/a/img'
        driver.find_element(By.XPATH, xp).click()

    def save_page(self, url, driver, filename="ee.html"):
        time.sleep(1)
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="tab"]/li[2]/a').click()
        time.sleep(2)

        open(f'{filename}', 'w+', encoding='utf-8')\
            .write(driver.page_source)

        print(f'{filename}(으)로 저장 했습니다.')

        exit(0)

    def get_target(self):
        # 쓸 책과 from, to 장을 정하는 기능
        # book의 전체 chapter보다는 작게
        #
        return {'book_name':'mat', 'from_chapter':14, 'to_chapter': 15}

    def send_message(self):
        msg = {
            0 : "오늘은 쓸게 없네요?",
            1 : "오늘은 안쓰는 날 입니다.",
            2 : "{}부터 {}까지 썼습니다."
        }


    def run(self, chapterUrl):
        self.driver.get(chapterUrl)

        ul = self.driver.find_element(By.CLASS_NAME,"write").find_element(By.TAG_NAME, "ul")
        lis = ul.find_elements(By.TAG_NAME, "li")

        print("절 수:", len(lis))

        for index in range(0, len(lis)):
            li = lis[index]
            ps = li.find_elements(By.TAG_NAME, "p")
            statement = ps[0].text
            rndInt = random.randint(2, 5)
            print("{}절 중 {}절 : rndSec:{}".format(len(lis), index+1, rndInt))
            textarea = ps[1].find_element(By.TAG_NAME, "textarea")
            time.sleep(rndInt)

            cnt = 0
            while (textarea.is_enabled() == False and cnt < 5):
                textarea = ps[1].find_element(By.TAG_NAME, "textarea")
                textarea.click()
                rndInt = random.randint(2, 5)
                print(f"------is_enabled() False then plus {rndInt} sec -----")
                time.sleep(rndInt)
                cnt += 1

            # print('statement:', statement)
            textarea.send_keys(statement)
            time.sleep(0.5)
            # print('before enter')
            textarea.send_keys('.')
            textarea.send_keys(Keys.BACKSPACE)
            textarea.send_keys(Keys.RETURN)
            time.sleep(0.5)

    def call(self, sub, cb_idx, book_cd, fr, to):

        for chapter in range(fr, to + 1):
            print("{}장".format(chapter))
            chapterUrl = f"http://bible.godpia.com/write/{sub}.asp?cb_idx={cb_idx}&ver=gae&vol={book_cd}&chap={chapter}&secindex=1"
            self.run(chapterUrl)
            time.sleep(60 * 6)

#1pe 벧전 #2pe벧후3 1jn요일 5 계rev
#창gen 출exo
godpia_writer = GodPiaBibleWriter('login')
t = godpia_writer.get_target()
godpia_writer.call('sub020302', '2386', 'gen', 47, 50)




