#np39.py
#39.Zipfの法則
"「単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．」"
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

dolist = []
for zip_ in catlist:
  for d in zip_:
    dolist.append(d['base'])
#collections.Counter()でリスト内の単語の出現頻度を出力し、
#most_common()で出現回数順に要素を取得。
from collections import Counter
f_most_common = [f[1] for f in Counter(dolist).most_common()]

#両対数グラフを表示。
import matplotlib.pyplot as plt
import numpy as np

plt.scatter(np.log(range(1, len(f_most_common)+1)), np.log(f_most_common))
plt.show();