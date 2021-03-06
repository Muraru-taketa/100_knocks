#np21.py
import pandas as pd #これ使うと色々抽出の指定が楽らしい
import re
#データフレームを今回は指定する
df = pd.read_json("jawiki-country.json", lines=True)#pandasでjsonファイルを読みこむときの型
#print(df.query('title=="イギリス"')['text'].values)
cat_txt = df.query('title=="イギリス"')['text'].values[0] #.queryを使うことで条件指定をできる
#今回はイギリスを含むものvaluesはデータの値Pandasを使うときに使うやつ。値を指定すると軸ラベルを削除できたりする。
#numpyを表現するためのもの。
a = r'\[\[Category:.*\]\]' #cat_txtで指定した物からCategoryに該当する物を抽出指定
for line in cat_txt.split('\n'):#改行分割をする
    result = re.match(a, line)#reモジュールと一緒に使うmatchは先頭がマッチするか調べる
    if result is not None: #resultがマッチした物でない物のときTrueにする
        print(line)
