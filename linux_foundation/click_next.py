from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import chromedriver_autoinstaller, time, os
from selenium.webdriver.common.by import By





if __name__ == "__main__":
    chromedriver_autoinstaller.install()

    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get("https://trainingportal.linuxfoundation.org")
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("oceanfog1@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(os.getenv("LINUX_FOUNDATION_PW"))
    driver.find_element(By.XPATH, '/html/body/app-root/cb-main-layout/div/div[2]/div/div[1]/div[2]/cb-login-controller/div/div[2]/div[1]/div/div/form/div[2]/div/div[4]/cb-button/button').click()

    time.sleep(1)
    # 들어가서 클릭
    url = 'https://trainingportal.linuxfoundation.org/learn/course/kubernetes-fundamentals-lfs258/api-objects/lab-exercises?page=1'
    driver.get(url)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, '')
    driver.find_element(By.XPATH, '//*[@id="ember5983"]/span[1]').click()

    time.sleep(100)

