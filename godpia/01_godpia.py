from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import random

chrome_options = Options()
# chrome_options.add_argument("--headless")

rootPath = ".."
driver = webdriver.Chrome(
    executable_path="{}/chrome/chromedriver74".format(rootPath),
    options=chrome_options
)

url = "http://bible.godpia.com/write/sub020301.asp?cb_idx=602"
driver.get(url)

driver.find_elements_by_class_name("h-btn01")[1]\
    .find_element_by_class_name("clickNavMenu").click()


driver.find_element_by_id("inputID")\
     .send_keys("oceanfog")
driver.find_element_by_id("inputPW") \
    .send_keys("4rhat1249")

driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/a/img").click()


def run(chapterUrl):
    driver.get(chapterUrl)

    ul = driver.find_element_by_class_name("write").find_element_by_tag_name("ul")
    lis = ul\
        .find_elements_by_tag_name("li")

    print("lis:", len(lis))

    for index in range(0, len(lis)):
        li = lis[index]
        ps = li.find_elements_by_tag_name("p")
        statement = ps[0].text
        rndInt = random.randint(3, 5)
        print("{}/{} : rndSec:{}".format(index+1, len(lis), rndInt))
        textarea = ps[1].find_element_by_tag_name("textarea")
        time.sleep(rndInt)

        if(textarea.is_enabled() == False):
            time.sleep(5)
        print(textarea.tag_name)
        print(textarea.is_enabled())
        print(textarea.is_selected())
        textarea.send_keys(statement)
        time.sleep(1)
        textarea.send_keys(Keys.RETURN)
        time.sleep(1)

for chapter in range(5, 5 + 1):
    print("{}장".format(chapter))
    chapterUrl = "http://bible.godpia.com/write/sub020302.asp?cb_idx=602&ver=gae&vol=mrk&chap={}&secindex=1".format(chapter)
    run(chapterUrl)
    time.sleep(20)




