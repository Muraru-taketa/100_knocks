#np49.py
"""
9. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiiとjj（ii<jj）のとき，係り受けパスは以下の仕様を満たすものとする．

問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を” -> “で連結して表現する
文節iiとjjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．

文節iiから構文木の根に至る経路上に文節jjが存在する場合: 文節iiから文節jjのパスを表示
上記以外で，文節iiと文節jjから構文木の根に至る経路上で共通の文節kkで交わる場合: 
文節iiから文節kkに至る直前のパスと文節jjから文節kkに至る直前までのパス，文節kkの内容を” | “で連結して表示
"""
from itertools import combinations#リストから順列を生成、列挙
import re

# 区切り文字
separator = re.compile('\t|,')
# かかりうけ
kakari =  re.compile(r'''(?:\*\s\d+\s) # キャプチャ対象外
                            (-?\d+)       # 数字(係り先)
                        ''', re.VERBOSE)

# 係り元を代入,Chunkリストを文のリストを追加
def append_sentence(chunks, sentences):

    # 係り元を代入
    for i, chunk in enumerate(chunks):
        if chunk.dst != -1:
            chunks[chunk.dst].srcs.append(i)
    sentences.append(chunks)
    return sentences

import np41sss

sentences = np41sss.Ai_morphs()
sentence = sentences[2]
rep = []
with open('./ans49.txt', 'w') as f:
    for i, chunk in enumerate(sentence):
        if '名詞' in [morph.pos for morph in chunk.morphs]:  # 名詞を含む文節
            rep.append(i)
    for i, j in combinations(rep, 2):  # 名詞を含む文節のペア作成
        path_i = []
        path_j = []
        while i != j:
            if i < j:
                path_i.append(i)
                i = sentence[i].dst
            else:
                path_j.append(j)
                j = sentence[j].dst
        if len(path_j) == 0:#文節iiから構文木の根に至る経路上に文節jjが存在する場合:
                            #文節iiから文節jjのパスを表示
            chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in sentence[path_i[0]].morphs])
            chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sentence[i].morphs])
            chunk_X = re.sub('X+', 'X', chunk_X)
            chunk_Y = re.sub('Y+', 'Y', chunk_Y)
            path_XY = [chunk_X] + [''.join(morph.surface for morph in sentence[s].morphs) for s in path_i[1:]] + [chunk_Y]
            print(' -> '.join(path_XY), file=f)
        else:#上記以外で，文節iiと文節jjから構文木の根に至る経路上で共通の文節kkで交わる場合:
            #文節iiから文節kkに至る直前のパスと文節jjから文節kkに至る直前までのパス，文節kkの内容を” | “で連結して表示
            chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in sentence[path_i[0]].morphs])
            chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sentence[path_j[0]].morphs])
            chunk_k = ''.join([morph.surface for morph in sentence[i].morphs])
            chunk_X = re.sub('X+', 'X', chunk_X)
            chunk_Y = re.sub('Y+', 'Y', chunk_Y)
            path_X = [chunk_X] + [''.join(morph.surface for morph in sentence[s].morphs) for s in path_i[1:]]
            path_Y = [chunk_Y] + [''.join(morph.surface for morph in sentence[s].morphs) for s in path_j[1:]]
            print(' | '.join([' -> '.join(path_X), ' -> '.join(path_Y), chunk_k]), file=f)