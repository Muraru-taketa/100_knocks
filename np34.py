#np34.py
"2つの名詞が「の」で連結されている名詞句を抽出せよ．"
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

AtoBlist = []#空のcatlistに形態素解析したものを入れてそのcatlistを今度は動詞だけ抜き出す別の箱を用意して入れる。

for line in catlist: #list indices must be integers or slices, not strと怒られる。インデックに文字列が指定されないようにする。ここ増やしたらいけた
    for atob in line:
        for i in range(len(atob)-2): 
            if (atob[i]["pos"] and atob[i+2]["pos"]) == "名詞" \
            and atob[i+1]["surface"] == "の":
                AtoBlist.append(atob[i]["surface"] +
                                atob[i+1]["surface"] +
                                atob[i+2]["surface"])
#のでくっつけられているものをリストで表示その中の名詞を取り出す。
#見つけたら取り出しくっつけ作業で表示させる。
set(AtoBlist)

# リストの最初の10個の集合を表示
print(set(AtoBlist))