#np43.py
#43. 名詞を含む文節が動詞を含む文節に係るものを抽出
"""名詞を含む文節が，動詞を含む文節に係るとき，
これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

import np41

sentences = np41.Ai_morphs()

sentence = sentences[2]
for chunk in sentence.chunks:
  if int(chunk.dst) != -1:
    modifier = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
    modifier_pos = [morph.pos for morph in chunk.morphs]
    modifiee = ''.join([morph.surface if morph.pos != '記号' else '' for morph in sentence.chunks[int(chunk.dst)].morphs])
    modifiee_pos = [morph.pos for morph in sentence.chunks[int(chunk.dst)].morphs]
    if '名詞' in modifier_pos and '動詞' in modifiee_pos:
      print(modifier, modifiee, sep='\t')