
**Translator used in the CLI environment**
=================================================
## Description
&nbsp;&nbsp;&nbsp;&nbsp;This project is just Toy Project which was developed for me to use. I can provide it if someone else wants to use it. I just write down the documents below just for the record.
## Motivation 
&nbsp;&nbsp;&nbsp;&nbsp;As I began to post my studies on this blog, I thought it was better to write in English. But my English composition was not so good. I wasn't sure if the sentence I worte was correct. So I frequent the Naver papago translator via a Web browser. and I spend more time translating than posting.
&nbsp;&nbsp;&nbsp;&nbsp;The posting is written using Markdown. I use the VS code + Markdown Extension with a terminal to write it. and I work in a CLI environment most of the time. That's why I thought I needed this project.
## What used?
- At first I tried to approach it using **'Selenium'** with headless chrome because I thought the other way was going to cost money. But it was too slow to use.
- So I thought it would be better to use [Naver's OpenAPI](https://developers.naver.com/main/).
- It was free and fast enough so I could use it satisfactor.
- I used regular expression to implement options features.
## Features
&nbsp;&nbsp;&nbsp;&nbsp;The ppg module has two features. The first is the **Language Detection** to detect which language the entered string is and the other is **Language translation** to translate it into the language you want. I was helped by the NAVER Papago openAPI to implement these features.
## Other
- **Install script**
    - It just change the 'ppg' module to executable file.
    - Then it copy the executable file and API key into the PATH(/usr/bin/share) for immediate use.
    - Then it make the symbolic link of the file in PATH(/usr/bin)
    - Finally, It create the uninstall script. It just help you delete the copied files.
## Result
- The use of **OpenAPI** was not as difficult as I thought, so it was easy to implement.
- Now I think it would be better to use Selenium only for **testing** or **crawling**.
## Installation
- You just run the script
```bash
~$ bash [papago-cli-path]/install.sh
```

## Uninstallation
- It provides a clear uninstall script. If you failed install it perfectly. you can run this script.
```bash
~$ bash [papago-cli-path]/uninstall.sh
```
## Support
- Now, the module only supports these languages. If there are people who need other language support, we will expand it further."
- Supported languages
    - Korean
    - English
    - Japanese
    
- Example of use
```bash
# Korean to English
user1234@DESKTOP:~$ ppg -e "안녕, 파파고!"

# English to Korean
user1234@DESKTOP:~$ ppg -k "Hi, Papago!"

# English to Japan
user1234@DESKTOP:~$ ppg -j "Hi, Papago!"
 
```
