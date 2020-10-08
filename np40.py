#np40.py
#40. 係り受け解析結果の読み込み（形態素）
"""
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），
品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，
各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．
"""
import re

morphs = []
sentences = []

# 区切り文字
separator = re.compile('\t|,')
# 除外行
exclude = re.compile(r'''EOS\n      # EOS, 改行コード
                         |          # OR
                         \*\s\d+\s  # '*, 空白, 数字１つ以上, 空白
                       ''', re.VERBOSE)
class Morph:
    def __init__(self, morph):

         #タブとカンマで分割
        tab = separator.split(morph)

        self.surface = tab[0] # 表層形(surface)
        self.base = tab[7]    # 基本形(base)
        self.pos = tab[1]     # 品詞(pos)
        self.pos1 = tab[2]    # 品詞細分類1(pos1)

words = []
morphs = []
with open('ai.ja.txt') as f:
  for line in f:#注文を文読み込んで生成していく
    if line[0] == '*':  # 係り受け関係を表す行：スキップ
      continue
    elif line != 'EOS\n':  # 文末以外：Morphを適用し形態素リストに追加
      morphs.append(Morph(line))
    else:  # 文末：形態素リストを文リストに追加
      words.append(morphs)
      morphs = []
#vars
#モジュール、クラス、インスタンス、あるいはそれ以外の dict 属性を持つオブジェクトの、 dict 属性を返します

for mor in words:
  print(vars(mor))