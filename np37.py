#np37.py
#37.「猫」と共起頻度の高い上位10語
"「「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．」"
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
#「猫」を含む文を抽出。
not_nekos = []
neko_lists = []
for word in catlist:
     for n in range(len(word)):
    #「base」の要素を取り出してリストに格納。
        not_nekos.append(word[n]['base'])
  #「猫」を含む文を抽出。
        if any(d['base'] == '猫' for d in word):
            neko_lists.append(word)
    #その中に出てくる「猫」以外の単語を抽出。
    #名詞を抜き出してみる。猫が名詞なので猫以外の名詞。*を除外。
            not_neko = [g['base'] for g in word if g['base'] != '猫' and g['pos'] == '名詞' and g['base'] != '*']
            not_nekos.extend(not_neko)

#collections.Counter()でリスト内の単語の出現頻度を出力。
from collections import Counter
f_not_nekos = Counter(not_nekos) 
f = list(zip(*f_not_nekos.most_common(10)))

#matplotlibでグラフの表示。
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font='IPAGothic')

labels = f[0]
height = f[1]
plt.bar(labels, height)
plt.show();