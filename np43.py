#np43.py
#43. 名詞を含む文節が動詞を含む文節に係るものを抽出
"""名詞を含む文節が，動詞を含む文節に係るとき，
これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

import re

# 区切り文字
separator = re.compile('\t|,')
# かかりうけ
kakari =  re.compile(r'''(?:\*\s\d+\s) # キャプチャ対象外
                            (-?\d+)       # 数字(係り先)
                        ''', re.VERBOSE)

class Morph:
    def __init__(self, morph):

        #タブとカンマで分割
        tab = separator.split(morph)

        self.surface = tab[0] # 表層形(surface)
        self.base = tab[6]    # 基本形(base)
        self.pos = tab[1]     # 品詞(pos)
        self.pos1 = tab[2]    # 品詞細分類1(pos1)

class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.srcs = []   # 係り元文節インデックス番号のリスト
        self.dst = dst  # 係り先文節インデックス番号
        self.phrase = ''.join([morph.surface for morph in morphs if morph.pos!='記号'])

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
for chunk in sentence.chunks:
  if int(chunk.dst) != -1:
    modifier = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
    modifier_pos = [morph.pos for morph in chunk.morphs]#記号等々の排除chunk,morphs内
    modifiee = ''.join([morph.surface if morph.pos != '記号' else '' for morph in sentence.chunks[int(chunk.dst)].morphs])
    modifiee_pos = [morph.pos for morph in sentence.chunks[int(chunk.dst)].morphs]
    if '名詞' in modifier_pos and '動詞' in modifiee_pos:#動詞と名詞を含むものを取り出す
      print(modifier, modifiee, sep='\t')#タブ区切り