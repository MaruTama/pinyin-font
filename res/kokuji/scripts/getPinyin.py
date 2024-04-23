from bs4 import BeautifulSoup
import requests

# ユーザーエージェントをFireFoxに変更ないとhtmlを取得できない
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
headers = {'User-Agent': ua}

def fetch_html(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'  # 文字コードをUTF-8に指定
        return response.text
    else:
        return None

# unicode は 87a9 のような形式で指定する
def get_pinyin_from_hancibao(unicode):
    base_url = 'https://www.hancibao.com/zi/'
    url = base_url + unicode
    html_content = fetch_html(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    label_cap = soup.find('span', class_='label-cap')
    if label_cap and label_cap.text == '拼音':
        pinyin = label_cap.find_next_sibling(text=True)
        return pinyin.strip()
    
# print(get_pinyin_from_hancibao('87a9'))
