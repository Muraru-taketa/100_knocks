#np31.py
#動詞の表層形をすべて抽出せよ．
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
        if line[0] != "\u3000":
            dic = {"surface": line[0],
                   "base": line[7], 
                   "pos": line[1],
                   "pos1": line[2]}
            #catlist.append(dic)
            linelist.append(dic)
        catlist.append(linelist)

# 最初の7行を表示
catlist[:7]
dolist = []#空のcatlistに形態素解析したものを入れてそのcatlistを今度は動詞だけ抜き出す別の箱を用意して入れる。

for line in catlist:
    for word in line:
        if word["pos"] == "動詞":#動詞をcatlistから抜き出す

            dolist.append(word["surface"])
        #print(line)
set(dolist)

# リストの最初の数個ほどの集合を表示
print(set(dolist[:11]))
