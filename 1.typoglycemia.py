#typoglycemia.py
import random

def Typoglycemia(txts):
#よくわからんので問題文をとりあえずコピペする
#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
#それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
#ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
#（例えば"I couldn't believe that I could actually understand what I was reading : 
#the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．'''
#??? とりあえず問題文を分解すると
#'''各単語の先頭と末尾のもじは残すと　dogだとdとgをとってoを残す
#注意：4文字以下はならべないが問題文を理解するために簡単な単語でたとえる
#dog,cat,bag,bedだとo,a,a,eとなってをそれをランダムに入れ替えというわけかなるほど'''
    result = []
    for word in txts.split(' '):#split:文字リストを分割
        if len(word) <= 5:#四文字以上の単語入れ替え対象
            result.append(word)#append:リストの末尾に要素を加える
        else:
            word_list = list(word[1:-1])#頭から最後まで
            random.shuffle(word_list)#入れ替え
            result.append(word[0] + ''.join(word_list) + word[-1])#append:リストの末尾に要素を加える
#joinは↑で取り出しました、文字列をランダムにしたのちに適当に連結させて文字列を作らせます。
    return ' '.join(result)
#またまた文章借ります。
txts = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantnm mechanics.'

result = Typoglycemia(txts)
print('ランダム:' + result)