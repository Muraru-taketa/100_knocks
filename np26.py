#np26.py
from collections import OrderedDict #OrderedDictを使うことで{}の中のkeyとvalueからなる、データが含まれるオブジェクト
from pprint import pprint #pprintでデータ出力の整然化インデントとか指定できるらしい
import re
import pandas as pd
df = pd.read_json("jawiki-country.json", lines=True)
mrk_uk = df.query('title=="イギリス"')['text'].values[0]
mark = re.search(r'^\{\{基礎情報.*?\n(.*?)\}\}$', mrk_uk, re.MULTILINE+re.VERBOSE+re.DOTALL)#.search先頭に限らずマッチするかチェック、抽出
patt = OrderedDict(re.findall(r'^\|(.+?)\s*=\s*(.+?)(?: (?=\n\|)| (?=\n$))', mark.group(1), re.MULTILINE+re.VERBOSE+re.DOTALL)) 
#findallで全てにマッチするものだけ取り出す。 
#MULTILINE指定で行毎の文字列の先頭」がマッチする
#VERBOSEで空白、コメントを無視する
#DOTALLで.を改行(\n)にマッチさせる。
# マークアップ除去
def rem_mark(string):

# 強調マークアップの除去
# 除去対象：''他との区別''、'''強調'''、'''''斜体と強調'''''
    replaced = re.sub(r'(\'{2,5})(.*?)(\1)', r'\2', string, flags=re.MULTILINE+re.VERBOSE)#sub関数は文字置換
#\1~9一致した文字列の１～９番目に対応する文字列に置換します。
#flags プログラムに与えるべき引数をコマンドラインから自動的に解析して取り出したり、指定されてなかったときにデフォルト値を定義できたり便利
    return replaced #replacedを定義して返して除去の力を持たせる。

for i, (key, value) in enumerate(patt.items()):#enumerate forループの中でリスト（配列）などのイテラブルオブジェクトの要素と同時にインデックス番号（カウント、順番）を取得できる。今回はマークアップ削除した物を順番を変えないでそのままの列順に並べてあげる
#items(): 各要素のキーkeyと値valueに対してforループ処理
    replaced = rem_mark(value)#key,valueを読み込みマークアップ除去状態を出す
    patt[key] = replaced
pprint(patt)
#(\'{2,5})    2〜5個の'（マークアップの開始）
#(.*?)        任意の1文字以上（対象の文字列）
#(\1)         1番目のキャプチャと同じ（マークアップの終了）
# ^\{\{基礎情報.*?\n  検索語句(\はエスケープ処理)、非キャプチャ、非貪欲
#(.*?)              任意の文字列
#\}\}               検索語句(\はエスケープ処理)
#$                  文字列の末尾
#^\|          \はエスケープ処理、非キャプチャ
#(.+?)        キャプチャ対象(key)、非貪欲
#\s*          空白文字0文字以上
#=            検索語句、非キャプチャ
#\s*          空白文字0文字以上
#(.+?)        キャプチャ対象(Value)、非貪欲
#(?:          キャプチャ対象外のグループ開始
# (?=\n\|)   改行(\n)+'|'の手前(肯定の先読み)
#| (?=\n$)    または、改行(\n)+終端の手前(肯定の先読み)
#)            キャプチャ対象外のグループ終了
'''flagsの使い方
# 定義用のflagを作成
flags = tf.app.flags

# 参照用のflagを作成
FLAGS = flags.FLAGS

# stringの定義
flags.DEFINE_string(定数名, 初期値, 説明文)

# floatの定義
flags.DEFINE_float(定数名, 初期値, 説明文)

# intの定義
flags.DEFINE_integer(定数名, 初期値, 説明文)

# boolの定義
flags.DEFINE_boolean(定数名, 初期値, 説明文)

# 定数の参照
print(FLAGS.定数名)
'''