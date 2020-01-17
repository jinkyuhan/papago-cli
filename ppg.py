from selenium import webdriver
from bs4 import BeautifulSoup

DEBUG = False

setting = webdriver.ChromeOptions()
setting.add_argument('headless')
# setting.add_argument('--no-sandbox')
setting.add_argument('window-size=1920x1080')
setting.add_argument('--disable-gpu')

driver = webdriver.Chrome('./chromedriver', options=setting)
try:
    driver.get('https://papago.naver.com/')
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.implicitly_wait(3)
    if DEBUG:
        print(soup)
    driver.get_screenshot_as_file("dbjg.png")
    driver.find_element_by_id("txtSource").send_keys('abcde')
# except:
#     print("fail")
finally:
    driver.quit()
