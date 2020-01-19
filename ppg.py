from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import re

DEBUG = False


def main(option, txt):
    p = re.compile('-[kej]')

    # Option exception
    if len(option) != 2 or not p.match(option):
        print("""
        !!![usage] You can select target language.
            -k: Korean
            -e: English
            -j: Japanese
        """)
    elif option[1] == 'k':
        print(translate('Korean', txt))
    elif option[1] == 'e':
        print(translate('English', txt))
    elif option[1] == 'j':
        print(translate('Japanese', txt))


def translate(target_lang, source_text) -> str:

    selectors = {
        "DropdownMenu": "#ddTargetLanguage2 > div.dropdown_top___13QlJ > button:nth-child(2)",
        "DropdownItem_Korean": "#ddTargetLanguage2 > div.dropdown_menu___XsI_h.active___3VPGL > ul > li.select_item___1U0X9.active___3VPGL > a",
        "DropdownItem_English": "#ddTargetLanguage2 > div.dropdown_menu___XsI_h.active___3VPGL > ul > li:nth-child(2) > a",
        "DropdownItem_Japanese": "#ddTargetLanguage2 > div.dropdown_menu___XsI_h.active___3VPGL > ul > li:nth-child(3) > a",
        "SourceText": "#txtSource",
        "TargetText": "#txtTarget",
        "TranslateButton": "#btnTranslate"
    }
    # chrome setting
    setting = webdriver.ChromeOptions()
    setting.add_argument('headless')
    setting.add_argument('window-size=1920x1080')
    setting.add_argument('--disable-gpu')

    # open papago page
    driver = webdriver.Chrome(
        '/home/jinkyuhan/Desktop/papago-cli/chromedriver.exe', options=setting)
    try:
        driver.get('https://papago.naver.com/')
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # select target language
        dropdown_menu = driver.find_element_by_css_selector(selectors["DropdownMenu"])
        dropdown_menu.click()
        dropdown_item = driver.find_element_by_css_selector(selectors["DropdownItem_"+target_lang])
        dropdown_item.click()

        # input text
        driver.find_element_by_css_selector(selectors["SourceText"]).send_keys(source_text)

        # Submmit
        translate_button = driver.find_element_by_css_selector(selectors["TranslateButton"])
        translate_button.click()
        if DEBUG:
            driver.get_screenshot_as_file("dbjg.png")

        # read result
        result = driver.find_element_by_css_selector(selectors["TargetText"]).text
    finally:
        driver.quit()

    return result


if __name__ == "__main__":

    # Excution arguments exception
    if len(sys.argv) != 3:
        print("""
        !!! usage: ppg [target_lang_option] [source_txt]
        """)
        sys.exit()
    main(sys.argv[1], sys.argv[2])
    main('-e', '안녕하세요')
