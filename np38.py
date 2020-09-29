#np38.py
#38.ヒストグラムPermalink
"「単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．」"
#表層(surface)：リスト[0]番目
#基本計(base)：リスト[7]番目
#品詞(pos)：リスト[1]番目
#品詞細分類1(pos1)：リスト[2]番目

cat = 'neko.txt.mecab'#catに格納
with open(cat)as f:
#1文ずつ区切って読み込み
    text = f.read().splitlines()
import re
#「\t」と「,」で分割してリスト化
nlist = [re.split("[\t|,]", lines) for lines in text]

catlist = []
for line in nlist:
    linelist = []
    if line[0] != "EOS":
         # 全角空白を除外
        #if line[0] != "\u3000":
        dic = {"surface": line[0],
                "base": line[7].replace('\n',''), 
                "pos": line[1],
                "pos1": line[2]}
            #catlist.append(dic)
        linelist.append(dic)
    catlist.append(linelist)
#「base」の単語を抽出。
histword = []
for word in catlist:
  for d in word:
    histword.append(d['base'])

#collections.Counter()でリスト内の単語の出現頻度を出力。
from collections import Counter
f_words = Counter(histword)

#matplotlibでヒストグラムの表示。
import matplotlib.pyplot as plt

plt.hist(f_words.values(), bins=10, range=(1,10))
plt.show();