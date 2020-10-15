#np41.py
"""40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストの係り受け解析結果を読み込み，
１文をChunkオブジェクトのリストとして表現し，
冒頭の説明文の文節の文字列と係り先を表示せよ．
本章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

def Ai_morphs():

    import re

    morphs = []
    sentences = []

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
        def __init__(self, morphs, srcs):
            self.morphs = morphs
            self.dst = []   # 係り元文節インデックス番号のリスト
            self.srcs = srcs  # 係り先文節インデックス番号

    # 係り元を代入,Chunkリストを文のリストを追加
    def append_sentence(chunks, sentences):

        # 係り元を代入
        for i, chunk in enumerate(chunks):
            if chunk.srcs != -1:
                chunks[chunk.srcs].dst.append(i)
        sentences.append(chunks)
        return sentences, []

    morphs = []
    chunks = []
    sentences = []

    with open('ai.ja.txt.parsed') as f:

        for line in f:
            bun = kakari.match(line)#係り受けにマッチするもの

            # もしEOSまたは係り受け解析結果ではないとき
            if not (line == 'EOS\n' or bun):
                morphs.append(Morph(line))

            # 反対にEOSまたは係り受け解析結果で、形態素解析結果があるとき
            elif len(morphs) > 0:
                chunks.append(Chunk(morphs, srcs))
                morphs = []

            # もし係り受け結果のとき
            if bun:
                srcs = int(bun.group(1))

            # もしEOSで係り受け結果があるとき
            if line == 'EOS\n' and len(chunks) > 0:
                sentences, chunks = append_sentence(chunks, sentences)
    return sentences
if __name__ == "__main__":
    sentences = Ai_morphs()
    for chunk in sentences[2]:
        print([morph.surface for morph in chunk.morphs], chunk.srcs, chunk.dst)    