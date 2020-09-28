#np35.py(34)
"名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．2015版のためここを34（２）とする"
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

longnlist = []
dolist = []

for line in catlist:
    for word in line:
        if word["pos"] == "名詞":
            longnlist.append(word["surface"])
        else:
            if word == []:
                continue
            elif len(word) > 1:
                longnlist.append("".join(word))
            dolist = []

set(longnlist)

# リストの最初の10個の集合を表示
print(set(longnlist[:10]))