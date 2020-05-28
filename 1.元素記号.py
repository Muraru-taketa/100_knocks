w = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
#連想配列？辞書型とかなんとか
words ={}
for i,word in enumerate(w.split(),1):#enumerate:組み込み関数forループカウンタの値をリストから取り出した要素と合わせて変数を取り出せる。
#split:区切り文字分割
    if i in (1, 5, 6, 7, 8, 9, 15, 16, 19):
        words[word[:1]] = i#strip():文字列の先頭と末尾にある余分な文字を取り除く。
    else:#:1先頭
        words[word[:2]] = i
    #:2先頭からインデックス1まで
print(words)