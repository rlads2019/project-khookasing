import requests
from bs4 import BeautifulSoup
import re
import os
from random import random
import time

#魔鏡歌詞網熱門華語男歌手的url
url = 'https://mojim.com/twza1.htm'

#取得根目錄
curDir = os.getcwd()

#取得所有男歌手的頁面
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
block = soup.find(class_="s_listA").find_all('a')

#創建資料夾
if not os.path.exists('超過100首'):
    os.mkdir('超過100首')
    print("Directory top100 Created ")
else:
    print("Directory top100 already exists")

curDir += "/超過100首"
os.chdir(curDir)

if not os.path.exists('男'):
    os.mkdir('男')
    print("Directory 男 Created ")
else:
    print("Directory 男 already exists")

if not os.path.exists('女'):
    os.mkdir('女')
    print("Directory 女 Created ")
else:
    print("Directory 女 already exists")

curDir += "/男"

os.chdir(curDir)

#將歌詞寫入檔案
def writeFile(i):
    #參數i: bs4中的<a> tag物件
    #取得歌詞內文
    j = i.get('href')
    sub_resp = requests.get("https://mojim.com" + j)
    sub_soup = BeautifulSoup(sub_resp.text, 'html.parser')
    sub_name = sub_soup.find('dd','fsZx3')
    title = i.get('title').split(' 歌')[0]
    if '/' in title:
        title=title.replace("/", "")
    path = title+ ".txt"
    f = open(path, 'w')
    if(sub_name!=None):

        s=str(sub_name)
        start = re.search("<br/><br/>",s).start()
        s=s[start:]
        sub_name = BeautifulSoup(s, 'html.parser')

        #文本處理，用正規表示刪除一些不必要的字彙
        if re.search("\[(([a-z]|\d|\:|\.|)+|([a-z]+:\S{1,4}))\]",sub_name.text)!=None:
            end = re.search("\[(([a-z]|\d|\:|\.|)+|([a-z]+:\S{1,4}))\]",sub_name.text).start()
            write = sub_name.text[:end]
            write = write.replace('更多更詳盡歌詞 在 ※ Mojim.com　魔鏡歌詞網',"")
            write = re.sub(r"感謝.{5,10}(修正|提供)歌詞", "", write)
            f.write(write)
        else:
            write = sub_name.text.replace('更多更詳盡歌詞 在 ※ Mojim.com　魔鏡歌詞網',"")
            write = re.sub(r"感謝.{5,20}(修正|提供)歌詞", "", write)
            f.write(write)


for i in block:
    j = i.get('href')
    resp = requests.get("https://mojim.com" + j)
    #歌手網址
    soup = BeautifulSoup(resp.text, 'html.parser')
    block3= soup.find_all('dd', 'hb2')
    block4 = soup.find_all('dd','hb3')


    # if i.text!='周華健' and i.text!='盧廣仲' and i.text!='隔壁老樊' and i.text!='伍佰' and i.text!='蕭煌奇' and i.text!='周杰倫' and i.text!='陳奕迅' and i.text!='林俊傑' and i.text!='林宥嘉' and i.text!='高爾宣' and i.text!='張學友' and i.text!='華晨宇' and i.text!='薛之謙' and i.text!='邱振哲' and i.text!='周興哲' and i.text!='陳零九' and i.text!='王力宏' and i.text!='劉德華' and i.text!='吳青峰' and i.text!='李榮浩' and i.text!='楊小壯':
    #     print(i.text)

    for i in block3:

        song_left = i.find_all('span','hc3')
        for j in song_left:
            sl = j.find_all('a')
            for k in sl:
               writeFile(k)

        song_right = i.find_all('span','hc4')
        for j in song_right:
            sr = j.find_all('a')
            for k in sr:
                writeFile(k)


    for i in block4:


        song_left = i.find_all('span','hc3')
        for j in song_left:
            sl = j.find_all('a')
            for k in sl:
               writeFile(k)

        song_right = i.find_all('span','hc4')
        for j in song_right:
            sr = j.find_all('a')
            for k in sr:
                writeFile(k)

    #random delay 避免被魔境網拒絕訪問            
    delay=round(random()*100)
    print(delay)
    time.sleep(delay)
