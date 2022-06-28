from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import random, os

import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

class GodPiaBibleWriter:

    def __init__(self, mode):
        chromedriver_autoinstaller.install()

        if mode == 'login':
            id = os.environ.get("GODPIA_ID")  # 환경변수 설정
            password = os.environ.get("GODPIA_PASSWORD")  # 환경변수 설정
            if id == None or password == None:
                print('id또는 패스워드를 입력해주세요')
                exit()
            driver = webdriver.Chrome(options=Options())
            self.login(driver, id, password)
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
            time.sleep(30)

#1pe 벧전 #2pe벧후3 1jn요일 5 계rev
#창gen
godpia_writer = GodPiaBibleWriter('login')
godpia_writer.call('sub020302', '2386', 'gen', 10, 11)




