from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random, os, requests, time

import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from godpia.parser import TargetSelector, Target

class GodPiaBibleWriter:

    def __init__(self, mode='LOGIN'):
        chromedriver_autoinstaller.install()

        if mode == 'LOGIN':
            print(os.environ)
            print("id:" + os.environ.get("GODPIA_ID"))
            id = os.environ.get("GODPIA_ID")  # 환경변수 설정
            password = os.environ.get("GODPIA_PASSWORD")  # 환경변수 설정

            if id == None or password == None:
                print('id또는 패스워드를 입력해주세요. 입력하는 방법은 READMD.md를 참고해주세요.')
                exit()
            options = Options()
            options.headless = True
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=options)
            self.login(driver, id, password)
            # self.save_page("http://bible.godpia.com/write/sub020301.asp?cb_idx=2386#tb02-tab-tab", driver, "신약_쓸장선택.html")

        elif mode == 'debug':
            chrome_options = Options()
            chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
            driver = webdriver.Chrome(options=chrome_options)

        self.driver = driver


    def login(self, driver, id, password):
        url = 'http://www.godpia.com/login/login_page.asp?ishref=http://bible.godpia.com/frameindex.asp?url_flag=/index.asp?&ipserver=bible.godpia.com'
        driver.get(url)


        driver.find_element(By.ID, "inputID").click()
        driver.find_element(By.ID, "inputID") \
            .send_keys(id)


        driver.find_element(By.ID, "inputPW").click()
        driver.find_element(By.ID, "inputPW") \
            .send_keys(password)

        # print(driver.page_source)

        xp = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/a/img'
        # driver.find_element(By.XPATH, xp).click()
        driver.execute_script("sendLogin();")

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

    def get_target(self) -> Target:
        # 쓸 책과 from, to 장을 정하는 기능
        url = "http://bible.godpia.com/write/sub020301.asp?cb_idx=2386"
        self.driver.get(url)

        self.driver.set_page_load_timeout(5)
        self.driver.find_element(By.XPATH, '//*[@id="tab"]/li[1]/a').click()
        ts = TargetSelector(self.driver.page_source) # 생성 할 때 구약 페이지
        self.driver.find_element(By.XPATH, '//*[@id="tab"]/li[2]/a').click()
        time.sleep(1)
        ts.parse(self.driver.page_source) # parse할 때 신약 페이지

        target:Target = ts.get_target_book_chapters()

        return target

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

    def call(self, sub, cb_idx, book_cd, chapters):
        print('GODPIA WRITE 시작')
        for chapter in chapters:
            print("{}장".format(chapter))
            chapterUrl = f"http://bible.godpia.com/write/{sub}.asp?cb_idx={cb_idx}&ver=gae&vol={book_cd}&chap={chapter}&secindex=1"
            self.run(chapterUrl)
            wait_sec = 60 * 6
            print(f'{wait_sec / 60}분을 기다립니다.')
            time.sleep(wait_sec)

#1pe 벧전 #2pe벧후3 1jn요일 5 계rev
#창gen 출exo
godpia_writer = GodPiaBibleWriter()

t:Target = godpia_writer.get_target()
godpia_writer.call('sub020302', '2386', t.sbn, t.chapters)

msg = f'{t.sbn} {t.chapters} FINISHED'
print(msg)
requests.get(
    f"https://api.telegram.org/bot281761192:AAE7h61HIio8eviXggpssYHrJJ58nHWT32A/sendMessage?chat_id=-1001595888089&text={msg}")
