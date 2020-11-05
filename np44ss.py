#np44.py
#44. 係り受け木の可視化
"""
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，Graphviz等を用いるとよい．
"""
#グラフを使うためのモジュール問題表記のものを使う(ネット参照)

import pydot_ng as pydot
from IPython.display import Image,display_png
from graphviz import Digraph
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
edges = []
for id, chunk in enumerate(sentence):
  if int(chunk.dst) != -1:
    modifier = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs] + ['(' + str(id) + ')'])
    modifiee = ''.join([morph.surface if morph.pos != '記号' else '' for morph in sentence[int(chunk.dst)].morphs] + ['(' + str(chunk.dst) + ')'])
    edges.append([modifier, modifiee])
n = pydot.Node('node')
n.fontname = 'IPAGothic'
graph = pydot.graph_from_edges(edges, directed=True)
graph.add_node(n)
graph.write_png('./kakarigi44.png')
display_png(Image('./kakarigi44.png'))