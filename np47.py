#np47.py
"""
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語（サ変接続名詞+を+動詞）
コーパス中で頻出する述語と助詞パターン
"""
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

with open('./ans47.txt', 'w') as f:
  for sentence in sentences:
    for chunk in sentence:
      for morph in chunk.morphs:
        if morph.pos == '動詞':  # chunkの左から順番に動詞を探す
            for i, src in enumerate(chunk.srcs):  # 見つけた動詞の係り元chunkが「サ変接続名詞+を」に
                if len(sentence[src].morphs) == 2 and sentence[src].morphs[0].pos1 == 'サ変接続' and sentence[src].morphs[1].surface == 'を':
                    sahen = ''.join([sentence[src].morphs[0].surface, sentence[src].morphs[1].surface, morph.base])
                    corpusses = []
                    kaihen = []
                    for src_sa in chunk.srcs[:i] + chunk.srcs[i + 1:]:
                        corpuss = [morph.surface for morph in sentence[src_sa].morphs if morph.pos == '助詞']
                        if len(corpuss) > 0:  
                            corpusses = corpuss + corpusses
                            kaihen.append(''.join(morph.surface for morph in sentence[src_sa].morphs if morph.pos != '記号'))
                    if len(corpusses) > 0: 
                        corpusses = sorted(list(set(corpusses)))# 助詞が見つかった場合はソートして出力
                        list_chunks = [morph.surface for morph in chunk.morphs]
                        chunks_line = "".join(list_chunks)
                        line = '{}\t{}\t{}'.format(chunks_line, ' '.join(kaihen), ' '.join(corpusses))
                        print(line, file=f)
                    break