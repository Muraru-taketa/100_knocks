#np23.py
import re
import pandas as pd
#ここらは一緒です。
df = pd.read_json("jawiki-country.json", lines=True)
sec_txt = df.query('title=="イギリス"')['text'].values[0]
ans = r'^(={2,})\s*(.+?)\s*\1$'#参照下
for line in sec_txt.split("\n"):#分割改行
    result = re.match(ans, line)
    if result is None: #resultがマッチしていれば返す
        #print(line)
        continue #このまま出してもまんまテキストでるだけそのためここで処理をスキップして
        #下の処理を行いセクションの抽出を行う
    print(result.group(2).strip(' ='), len(result.group(1)))#g２はレベルが＝＝の数でg１は見出しの抽出      
#^          文字列の先頭
#(={2,})    キャプチャ対象、2回以上の'='
#\s*        非キャプチャ、余分な0個以上の空白
#(.+?)      キャプチャ対象、任意の文字が1文字以上
#\s*        非キャプチャ、余分な0個以上の空白
#\1         後方参照、1番目のキャプチャ対象(={2,})と同じ内容
#$          行末