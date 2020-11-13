"""
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），
          係り先文節インデックス番号（dst），
          係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストの係り受け解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，
冒頭の説明文の文節の文字列と係り先を表示せよ．本章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

"""
• 今読んでる文節の文節番号と係り先番号がわかった時点で、この2つ (chunk_id, dst) を覚えておく
• elseのほうで次々にMorphを作っていく。このMorphのリスト (morphs) も覚えておく
• 次の文節に来たら Chunk(chunk_id, dst, morphs) を作ってsentenceリストにappend
• 一文読み終えたら（EOSが来たら）各Chunkのsrcsを埋めていく
とか、
• 今読んでる文節の文節番号と係り先番号がわかった時点で、`Chunk(chunk_id, dst, morphs=[])` を作ってsentenceリストにappend
• elseのほうでMorphを作っていく。作ったMorphは毎回sentence[-1] (== 今見ているChunk) のmorphsにappendしていく
• 一文読み終えたら（EOSが来たら）各Chunkのsrcsを埋めていく
"""

# * 0 17D 1/1 0.388993
from collections import defaultdict

class Morph:
    #表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
    def __init__(self, surface, base, pos, pos1):
        #初期化
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def __str__(self):
         return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'.format(self.surface, self.base, self.pos, self.pos1)

class Chunk:
    #形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst）， 係り元文節インデックス番号のリスト（srcs）
    def __init__(self, morphs ,dst, srcs):
        #self.chunk_id = chunk_id
        self.morphs = morphs
        self.dst = dst
        #self.srcs = srcs
        self.srcs = []
sentence = []
sentences = []
morphs = []
srcs = defaultdict(list)
filename = 'ai.ja.txt.parsed'
with open(filename, 'r') as f:
    for line in f:
        member = line.split()
        if line[0] == '*':
            num = int(member[1])
            dst = int(member[2].rstrip('D'))
            if dst != -1:
                srcs[dst].append(num)
            sentence.append(Chunk(morphs, dst, srcs[num]))
        elif line != 'EOS\n':
            ot = member[1].strip().split(',')  #baseに「\n*」って確か出てきてしまったから消すためにストリップ使用
            morphs.append(Morph(member[0], ot[6], ot[0], ot[1]))
        else:
            srcs.clear()
            morphs = []
            sentences.append(sentence)
            #morphs = []
            sentence = []

for num in sentences[2]:
    print(vars(num))
