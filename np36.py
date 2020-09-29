#np36.py
#matplotlibというやつをpipでインストールしてくるこれでグラフを生成できるらしい
#日本語の文字出力が必要なので!pip install japanize_matplotlibこれで
#IPAexフォントを使うと日本語でグラフを出力できるのでダウンロードする。
#36.頻度上位10語
"「出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．」"
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

words = []
for most in catlist:
  for n in range(len(most)):
    #「base」の要素を取り出してリストに格納。
    words.append(most[n]['base'])
#collections.Counter()でリスト内の単語の出現頻度を出力。
from collections import Counter
most_word = Counter(words)
#出現頻度が高い10語とその出現頻度の表示。most_common()
most_word.most_common(10)
#上位10単語とその頻度をそれぞれリストに格納。
f_lists = list(zip(*most_word.most_common(10)))

#matplotlibでグラフの表示します。
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font='IPAGothic')

labels = f_lists[0]
height = f_lists[1]
plt.bar(labels, height)
plt.show();