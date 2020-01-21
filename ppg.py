#!/usr/bin/python3

import os
import sys
import json
import re
from urllib import request
DEBUG = False


def detect_language(text):
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    data = 'query="{}"'.format(text)
    req = request.Request(url)
    req.add_header("X-Naver-Client-Id", CLIENT_ID)
    req.add_header("X-Naver-Client-Secret", CLIENT_SECRET)
    res = request.urlopen(req, data=data.encode("utf-8"))
    res_code = res.getcode()
    if(res_code == 200):  # success
        res_body = res.read()
        dec_data = res_body.decode('utf-8')
        if DEBUG:
            print("[Response] detected_lang: ", dec_data)
        detected_lang = json.loads(dec_data)["langCode"]
        return detected_lang
    else:  # fail
        print("! ERROR CODE: ", res_code)
        sys.exit()


def translate(target_lang, source_text):
    source_lang = detect_language(source_text)
    if source_lang == target_lang:
        print("! BAD OPTION: The source_lang and target_lang could not be same")
        sys.exit()
    url = "https://openapi.naver.com/v1/papago/n2mt"
    data = 'source={}&target={}&text="{}"'.format(
        source_lang, target_lang, source_text)
    req = request.Request(url)
    req.add_header("X-Naver-Client-Id", CLIENT_ID)
    req.add_header("X-Naver-Client-Secret", CLIENT_SECRET)
    res = request.urlopen(req, data=data.encode("utf-8"))
    res_code = res.getcode()
    if(res_code == 200):  # success
        res_body = res.read()
        dec_data = res_body.decode('utf-8')
        if DEBUG:
            print("[Response] translated_txt:", dec_data)
        translated_text = json.loads(
            dec_data)["message"]["result"]["translatedText"]
        return translated_text
    else:  # fail
        print("! ERROR CODE: ", res_code)
        sys.exit()


def get_api_key():
    with open('./API_key.json') as API_key:
        key = json.load(API_key)
    return key


def main(option, txt):

    if option[1] == 'k':
        print(translate('ko', txt))
    elif option[1] == 'e':
        print(translate('en', txt))
    elif option[1] == 'j':
        print(translate('ja', txt))


if __name__ == "__main__":

    # Bad arguments exception
    p = re.compile('-[kej]')

    if len(sys.argv) != 3 or len(sys.argv[1]) != 2 or not p.match(sys.argv[1]):
        print("""
        Bad arugments ERROR!

        Usage: ppg [target_lang_option] "[source_txt]"
         
        You have to select target language and use double quatoation for blank of source_txt.
            -k: Korean
            -e: English
            -j: Japanese
        
        You have to use Double quotation mark for source_txt like this
            ~/$ ppg -k "hello"
        """)
        sys.exit()
    
    key = get_api_key()
    CLIENT_ID = key['client_id']
    CLIENT_SECRET = key['client_secret']

    main(sys.argv[1], sys.argv[2])
