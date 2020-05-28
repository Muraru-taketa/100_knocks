#N_gram.py
#owakatiの分かち書きをする。uni=1,bi=2 tri=3
'''どうやったら分かち書きになるか
今日は眠いをbigramに手動ですると
今日、日は、は眠、眠い
今で始まって日で終わる感じで定義する。'''
def n_gram(txt, n):
#n=n_garmのn
    result = []
    for i in range(0, len(txt) - n + 1):#例：今日という単語からn個(2)-で+1すると日から始まる
        result.append(txt[i:i + n])
#iで始まってi+n(nは指定分割個数的なやつ)
    return result

txt = "I am an NLPer"
words = txt.split(' ')
#文字分け
print(n_gram(txt, 2))
#単語
print(n_gram(words, 2))