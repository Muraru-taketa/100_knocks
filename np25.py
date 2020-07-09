#np25.py
from collections import OrderedDict #OrderedDictを使うことで{}の中のkeyとvalueからなる、データが含まれるオブジェクト
from pprint import pprint #pprintでデータ出力の整然化インデントとか指定できるらしい
#今回は基礎情報の抽出要素と辞書型にする二つを扱う。順序を保持できる
import re
import pandas as pd
#ここらは一緒です。
df = pd.read_json("jawiki-country.json", lines=True)
tmp_uk = df.query('title=="イギリス"')['text'].values[0]
#uktmp = tmp_uk.split('\n')#分割改行
key = re.search(r'^\{\{基礎情報.*?\n(.*?)\}\}$',tmp_uk, re.MULTILINE+re.VERBOSE+re.DOTALL)#.search先頭に限らずマッチするかチェック、抽出
pprint(key.group(1))
value = OrderedDict(re.findall(r'^\|(.+d?)\s*=\s*(.+?)(?:(?=\n\|)| (?=\n$))', key[0], re.MULTILINE+re.VERBOSE+re.DOTALL))
#findallで全てにマッチするものだけ取り出す。
pprint(value)
#MULTILINE指定で行毎の文字列の先頭」がマッチする
#VERBOSEで空白、コメントを無視する
#DOTALLで.を改行(\n)にマッチさせる。
#はいsplit('\n')要らんくなった。
# ^\{\{基礎情報.*?\n  検索語句(\はエスケープ処理)、非キャプチャ、非貪欲
#(.*?)              任意の文字列
#\}\}               検索語句(\はエスケープ処理)
#$                  末尾
#^\|         \はエスケープ処理、非キャプチャ
#(.+?)        キャプチャ対象(key)、非貪欲
#\s*          空白文字0文字以上
#=            検索語句、非キャプチャ
#\s*          空白文字0文字以上
#(.+?)        キャプチャ対象(Value)、非貪欲
#(?:          キャプチャ対象外のグループ開始
#(?=\n\|)   改行(\n)+'|'の手前(肯定の先読み)
#| (?=\n$)    または、改行(\n)+終端の手前(肯定の先読み)
#)            キャプチャ対象外のグループ終了