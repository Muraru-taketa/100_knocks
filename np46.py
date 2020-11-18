#np46.py
#46. 動詞の格フレーム情報の抽出
'''
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
'''
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

with open('./ans46.txt', 'w') as f:
  for sentence in sentences:
    for chunk in sentence:
      for morph in chunk.morphs:
        if morph.pos == '動詞':  # chunkの左から順番に動詞を探す
          corpusses = []
          kaihen = []
          for src in chunk.srcs:  # 見つけた動詞の係り元chunkから助詞を探す
            corpuss = [morph.surface for morph in sentence[src].morphs if morph.pos == '助詞']
            if len(corpuss) > 0:  
                corpusses = corpuss + corpusses
                kaihen.append(''.join(morph.surface for morph in sentence[src].morphs if morph.pos != '記号'))
            if len(corpusses) > 0: 
                corpusses = sorted(list(set(corpusses)))# 助詞が見つかった場合はソートして出力
                list_chunks = [morph.surface for morph in chunk.morphs]
                chunks_line = "".join(list_chunks)
                line = '{}\t{}\t{}'.format(chunks_line, ' '.join(corpusses), ' '.join(kaihen))
                print(line, file=f)
            break