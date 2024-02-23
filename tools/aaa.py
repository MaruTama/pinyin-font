with open('waseikanji.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

# 先頭と末尾に '|' を追加
new_lines = ['|' + line + '|' for line in lines]

# 結果を新しいファイルに出力
with open('waseikanji.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))