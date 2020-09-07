from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('../chrome/chromedriver', options=chrome_options)

# 디버그 모드 chrome에서 로그인을 하신 후 실행 하세요.
url = 'https://ceo.baemin.com/self-service/orders/tax'

driver.get(url)

# 2분기
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/label[2]/p').click()
time.sleep(1)
# 조회 클릭
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div[1]/div[1]/div/button').click()