#np42.py
#42. 係り元と係り先の文節の表示
"""係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
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
for chunk in sentence:
    if int(chunk.dst) != -1:
        modifier = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
        modifiee = ''.join([morph.surface if morph.pos != '記号' else '' for morph in sentence[int(chunk.dst)].morphs])
        print(modifier, modifiee, sep='\t')