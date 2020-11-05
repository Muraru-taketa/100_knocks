#np45.py
"""
---45.動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． 
ただし，出力は以下の仕様を満たすようにせよ．

・動詞を含む文節において，最左の動詞の基本形を述語とする
・述語に係る助詞を格とする
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
・コーパス中で頻出する述語と格パターンの組み合わせ
・「行う」「なる」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
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
        self.doshi = ''
        self.zyoshi = ''

        for morph in morphs:            
            if morph.pos != '記号':
                self.zyoshi = '' #記号を取り除いた行
            if morph.pos == '句点':
                self.zyoshi = ''

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

with open('./ans45.txt', 'w') as f:
  for sentence in sentences:
    for chunk in sentence:
      for morph in chunk.morphs:
        if morph.pos == '動詞':  # chunkの左から順番に動詞を探す
          corpass = []
          for src in chunk.srcs:  # 見つけた動詞の係り元chunkから助詞を探す
            corpass = corpass + [morph.surface for morph in sentence[src].morphs if morph.pos == '助詞']
          if len(corpass) > 0:  # 助詞が見つかった場合はソートして出力
            corpass = sorted(list(set(corpass)))
            line = '{}\t{}'.format(morph.base, ' '.join(corpass))
            print(line, file=f)
          break
