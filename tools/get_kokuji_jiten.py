#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'  # 文字コードをUTF-8に指定
        return response.text
    else:
        return None

def extract_related_characters(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Initialize variables to hold the character and its related characters and variants
    related_chars = []
    variants = []
    
    # Extract related characters
    for idx, row in enumerate(soup.select('table tr')):
        cells = row.find_all('td')
        if len(cells) > 1:
            text = cells[0].text.strip().split("異体字: ")
            # 関連字
            if idx == 0:
                related_chars.append(text[0].replace("関連字:","").split(' ')[0])
            elif idx == 1:
                variants.append(text[0].replace("異体字:","").split(' ')[0])
            else:
                variants.append(text[0].split(' ')[0])

    # Generate the Unicode code points for the related characters and variants
    related_unicode  = [f"{char} U+{ord(char):X}" for char in related_chars] if len(related_chars) else ["NONE"]
    variants_unicode = [f"{char} U+{ord(char):X}" for char in variants] if len(variants) else ["NONE"]
    
    # Create the output string
    output_str = f"関連字: {', '.join(related_unicode)},  異体字: {', '.join(variants_unicode)}"
    
    return output_str

# [国字の字典](https://glyphwiki.org/wiki/Group:%E5%9B%BD%E5%AD%97%E3%81%AE%E5%AD%97%E5%85%B8)
# 処理するページのリスト
base_url = 'https://glyphwiki.org/wiki/kokuji-no-jiten-'
page_numbers = range(1, 1557)  # 0001 to 1556
# page_numbers = [1,17,19]

# 各ページに対して処理
for page_number in page_numbers:
    url = f"{base_url}{str(page_number).zfill(4)}"  # ゼロ埋めして4桁にする

    html_content = fetch_html(url)
    result = extract_related_characters(html_content)
    print("{:4d}: {}".format(page_number, result))
