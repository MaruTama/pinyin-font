# import requests
# from bs4 import BeautifulSoup

# # Unicode を 10進数に変換
# unicode_val = '206A4'
# decimal_val = int(unicode_val, 16)

# # URL を作成
# url = 'https://jigen.net/kanji/' + str(decimal_val)

# # リクエストを送信
# response = requests.get(url)
# html_content = response.text

# # BeautifulSoup インスタンスを作成
# soup = BeautifulSoup(html_content, 'html.parser')

# # '音訓未整理' を取得
# onkun_section = soup.find('dt', string='音訓未整理')
# if onkun_section != None:
#     onkun_items = onkun_section.find_next_sibling('dd').select('ul.nolist > li')
#     onkun = ','.join([item.text for item in onkun_items])
# else:
#     onkun = "NONE"

# # '発音' を取得
# pronounce_section = soup.find('dt', string='発音')
# if pronounce_section != None:
#     pronounce_items = pronounce_section.find_next_sibling('dd').select('ul.nolist > li')
#     pronounce = ', '.join([item.text for item in pronounce_items])
# else:
#     pronounce = "NONE"
# print('音訓未整理:{} 発音:{}'.format(onkun, pronounce))

import requests
from bs4 import BeautifulSoup

# ファイルをオープンし、各行をリストとして読み込む
with open('res/kokuji/kokuji_list_of_jigen-net.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

for line in lines:
    id, char, uni_code = line.split(' ')

    # Unicodeを10進数に変換
    decimal_val = int(uni_code[2:], 16)

    # URLを作成
    url = 'https://jigen.net/kanji/' + str(decimal_val)

    # リクエストを送信
    response = requests.get(url)
    html_content = response.text

    # BeautifulSoupインスタンスを作成
    soup = BeautifulSoup(html_content, 'html.parser')

    # '音訓未整理'を取得
    onkun_section = soup.find('dt', string='音訓未整理')
    if onkun_section is not None:
        onkun_items = onkun_section.find_next_sibling('dd').select('ul.nolist > li')
        onkun = ','.join([item.text for item in onkun_items])
    else:
        onkun = "NONE"

    # '発音'を取得
    pronounce_section = soup.find('dt', string='発音')
    if pronounce_section is not None:
        pronounce_items = pronounce_section.find_next_sibling('dd').select('ul.nolist > li')
        pronounce = ', '.join([item.text for item in pronounce_items])
    else:
        pronounce = "NONE"
    
    # 結果を出力
    print('|{}|{}|{}|音訓未整理:{}|発音:{}|'.format(id, char, uni_code, onkun, pronounce))