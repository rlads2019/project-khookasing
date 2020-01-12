import requests
from bs4 import BeautifulSoup
import re
import os
import time


url = 'https://mojim.com/twza1.htm'
curDir = os.getcwd()
sleep_count = 0

#使用方法：直接compile這個檔案
# python3 mojim_crawler.py

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

block = soup.find(class_="s_listA").find_all('a')


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


curDir += "/女"


os.chdir(curDir)




def writeFile(i):
        #print('hi')
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


            if re.search("\[(([a-z]|\d|\:|\.|)+|([a-z]+:\S{1,4}))\]",sub_name.text)!=None:
                end = re.search("\[(([a-z]|\d|\:|\.|)+|([a-z]+:\S{1,4}))\]",sub_name.text).start()
                write = sub_name.text[:end]
                write = write.replace('更多更詳盡歌詞 在 ※ Mojim.com　魔鏡歌詞網',"")
                write = re.sub(r"感謝.{5,10}(修正|提供)歌詞", "", write)



                f.write(write)
                print(i.get('title').split('歌')[0])
                print(write)
            else:
                write = sub_name.text.replace('更多更詳盡歌詞 在 ※ Mojim.com　魔鏡歌詞網',"")
                write = re.sub(r"感謝.{5,20}(修正|提供)歌詞", "", write)
                f.write(write)
                print(i.get('title').split(' 歌')[0])
                print(write)


# artists =  ['https://mojim.com/twh100951.htm', 'https://mojim.com/twh100111.htm', 
#             'https://mojim.com/twh102520.htm', 'https://mojim.com/twh221257.htm', 
#             'https://mojim.com/twh105350.htm', 'https://mojim.com/twh100092.htm', 
#             'https://mojim.com/twh134270.htm', 'https://mojim.com/twh105713.htm', 
#             'https://mojim.com/twh126832.htm', 'https://mojim.com/twh134046.htm', 
#             'https://mojim.com/twh109237.htm', 'https://mojim.com/twh100015.htm', 
#             'https://mojim.com/twh100162.htm', 'https://mojim.com/twh120572.htm', 
#             'https://mojim.com/twh219250.htm', 'https://mojim.com/twh229654.htm', 
#             'https://mojim.com/twh222104.htm', 'https://mojim.com/twh105044.htm', 
#             'https://mojim.com/twh100026.htm', 'https://mojim.com/twh102372.htm', 
#             'https://mojim.com/twh100052.htm', 'https://mojim.com/twh105661.htm', 
#             'https://mojim.com/twh208970.htm', 'https://mojim.com/twh118824.htm', 
#             'https://mojim.com/twh100087.htm', 'https://mojim.com/twh102386.htm', 
#             'https://mojim.com/twh109369.htm', 'https://mojim.com/twh187679.htm', 
#             'https://mojim.com/twh101187.htm', 'https://mojim.com/twh102201.htm', 
#             'https://mojim.com/twh100018.htm', 'https://mojim.com/twh172927.htm', 
#             'https://mojim.com/twh100239.htm', 'https://mojim.com/twh128710.htm', 
#             'https://mojim.com/twh100294.htm', 'https://mojim.com/twh100183.htm', 
#             'https://mojim.com/twh100091.htm', 'https://mojim.com/twh104316.htm', 
#             'https://mojim.com/twh106630.htm', 'https://mojim.com/twh219367.htm', 
#             'https://mojim.com/twh100085.htm', 'https://mojim.com/twh100199.htm', 
#             'https://mojim.com/twh100193.htm', 'https://mojim.com/twh100105.htm', 
#             'https://mojim.com/twh100171.htm', 'https://mojim.com/twh100207.htm', 
#             'https://mojim.com/twh105175.htm', 'https://mojim.com/twh100155.htm', 
#             'https://mojim.com/twh219544.htm', 'https://mojim.com/twh100041.htm', 
#             'https://mojim.com/twh106665.htm', 'https://mojim.com/twh100970.htm', 
#             'https://mojim.com/twh101604.htm', 'https://mojim.com/twh158190.htm', 
#             'https://mojim.com/twh108675.htm', 'https://mojim.com/twh108483.htm', 
#             'https://mojim.com/twh100923.htm', 'https://mojim.com/twh100040.htm', 
#             'https://mojim.com/twh105550.htm', 'https://mojim.com/twh100468.htm', 
#             'https://mojim.com/twh102242.htm', 'https://mojim.com/twh107602.htm', 
#             'https://mojim.com/twh100446.htm', 'https://mojim.com/twh215309.htm', 
#             'https://mojim.com/twh104266.htm', 'https://mojim.com/twh219468.htm', 
#             'https://mojim.com/twh100467.htm', 'https://mojim.com/twh219328.htm', 
#             'https://mojim.com/twh101024.htm', 'https://mojim.com/twh100028.htm', 
#             'https://mojim.com/twh104500.htm', 'https://mojim.com/twh109372.htm', 
#             'https://mojim.com/twh223372.htm', 'https://mojim.com/twh100055.htm', 
#             'https://mojim.com/twh101189.htm', 'https://mojim.com/twh100104.htm', 
#             'https://mojim.com/twh101117.htm', 'https://mojim.com/twh125153.htm', 
#             'https://mojim.com/twh102232.htm', 'https://mojim.com/twh101065.htm']


artists = [ # 'https://mojim.com/twh105703.htm', 'https://mojim.com/twh100463.htm', 
            # 'https://mojim.com/twh104613.htm', 'https://mojim.com/twh100095.htm', 
            # 'https://mojim.com/twh105272.htm', 'https://mojim.com/twh100090.htm', 
            # 'https://mojim.com/twh100163.htm', 'https://mojim.com/twh100229.htm', 
            # 'https://mojim.com/twh104821.htm', 'https://mojim.com/twh100019.htm', 
            # 'https://mojim.com/twh105599.htm', 'https://mojim.com/twh100663.htm', 
            # 'https://mojim.com/twh108440.htm', 'https://mojim.com/twh100098.htm', 
            # 'https://mojim.com/twh109122.htm', 'https://mojim.com/twh100233.htm', 
            # 'https://mojim.com/twh218008.htm', 'https://mojim.com/twh104279.htm', 
            # 'https://mojim.com/twh100515.htm', 'https://mojim.com/twh217658.htm', 
            # 'https://mojim.com/twh100312.htm', 'https://mojim.com/twh100166.htm', 
            # 'https://mojim.com/twh100170.htm', 'https://mojim.com/twh100115.htm', 
            # 'https://mojim.com/twh100143.htm', 'https://mojim.com/twh100062.htm', 
            # 'https://mojim.com/twh122960.htm', 'https://mojim.com/twh100142.htm', 
            # 'https://mojim.com/twh100158.htm', 'https://mojim.com/twh222189.htm', 
            # 'https://mojim.com/twh100131.htm', 'https://mojim.com/twh105079.htm', 
            # 'https://mojim.com/twh100096.htm', 'https://mojim.com/twh100954.htm', 
            # 'https://mojim.com/twh202390.htm', 'https://mojim.com/twh213714.htm', 
            # 'https://mojim.com/twh100287.htm', 'https://mojim.com/twh109601.htm', 
            # 'https://mojim.com/twh118727.htm', 'https://mojim.com/twh108050.htm', 
            # 'https://mojim.com/twh109805.htm', 'https://mojim.com/twh102453.htm', 
            # 'https://mojim.com/twh100187.htm', 'https://mojim.com/twh104942.htm', 
            # 'https://mojim.com/twh100285.htm', 'https://mojim.com/twh104870.htm', 
            # 'https://mojim.com/twh109907.htm', 'https://mojim.com/twh135268.htm', 
            # 'https://mojim.com/twh100313.htm', 'https://mojim.com/twh137200.htm', 
            # 'https://mojim.com/twh104479.htm', 'https://mojim.com/twh136088.htm', 
            # 'https://mojim.com/twh217840.htm', 'https://mojim.com/twh224154.htm', 
            # 'https://mojim.com/twh100173.htm', 'https://mojim.com/twh107683.htm', 
            # 'https://mojim.com/twh199951.htm', 'https://mojim.com/twh100093.htm', 
            # 'https://mojim.com/twh100593.htm', 'https://mojim.com/twh100074.htm', 
            'https://mojim.com/twh100117.htm', 'https://mojim.com/twh119630.htm', 
            'https://mojim.com/twh169562.htm', 'https://mojim.com/twh102140.htm', 
            'https://mojim.com/twh105635.htm', 'https://mojim.com/twh116318.htm', 
            'https://mojim.com/twh101930.htm', 'https://mojim.com/twh100708.htm', 
            'https://mojim.com/twh100255.htm', 'https://mojim.com/twh102407.htm', 
            'https://mojim.com/twh170380.htm', 'https://mojim.com/twh124798.htm', 
            'https://mojim.com/twh107721.htm', 'https://mojim.com/twh136359.htm', 
            'https://mojim.com/twh100089.htm', 'https://mojim.com/twh100156.htm', 
            'https://mojim.com/twh104518.htm', 'https://mojim.com/twh100102.htm', 
            'https://mojim.com/twh100340.htm', 'https://mojim.com/twh219014.htm']

# for i in block:
#     j = i.get('href')
#     resp = requests.get("https://mojim.com" + j)
#     #歌手網址
#     ...
for i in artists:
    resp = requests.get(i)
    #歌手網址
    soup = BeautifulSoup(resp.text, 'html.parser')
    block3= soup.find_all('dd', 'hb2')
    block4 = soup.find_all('dd','hb3')





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
                #sleep
                sleep_count += 1
                if sleep_count >100:
                   time.sleep(3)
                   sleep_count = 0
                writeFile(k)

        song_right = i.find_all('span','hc4')
        for j in song_right:
            sr = j.find_all('a')
            for k in sr:
                #sleep
                sleep_count += 1
                if sleep_count >100:
                   time.sleep(3)
                   sleep_count = 0
                writeFile(k)
