#np48.py
"""
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を” -> “で連結する
"""
#42を->で出せということかna

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
sentence = sentences[1]
with open('./ans48.txt', 'w') as f:
  for chunk in sentence:
    if '名詞' in [morph.pos for morph in chunk.morphs]:  # chunkが名詞を含むか確認
      path = [''.join(morph.surface for morph in chunk.morphs if morph.pos != '記号')]
      while chunk.dst != -1:  # 名詞を含むchunkを先頭に、dstを根まで順に辿ってリストに追加
        path.append(''.join(morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != '記号'))
        chunk = sentence[chunk.dst]
      print(' -> '.join(path), file=f)