#np29.py
from collections import OrderedDict #OrderedDictを使うことで{}の中のkeyとvalueからなる、データが含まれるオブジェクト
import re 
import requests#Requests を使うとWebサイトの情報取得や画像の収集などを簡単に行うことができる

import pandas as pd
df = pd.read_json("jawiki-country.json", lines=True)
hata_uk = df.query('title=="イギリス"')['text'].values[0]
naibu = re.search(r'^\{\{基礎情報.*?\n(.*?)\}\}$', hata_uk, re.MULTILINE+re.VERBOSE+re.DOTALL)#.search先頭に限らずマッチするかチェック、抽出
patt = OrderedDict(re.findall(r'^\|(.+?)\s*=\s*(.+?)(?: (?=\n\|)| (?=\n$))', naibu.group(1), re.MULTILINE+re.VERBOSE+re.DOTALL)) 
#findallで全てにマッチするものだけ取り出す。 
#MULTILINE指定で行毎の文字列の先頭」がマッチする
#VERBOSEで空白、コメントを無視する
#DOTALLで.を改行(\n)にマッチさせる。
# マークアップ除去
def rem_mark(string):

    # 強調マークアップの除去 
    # 除去対象：''他との区別''、'''強調'''、'''''斜体と強調'''''
    replaced = re.sub(r'(\'{2,5})(.*?)(\1)', r'\2', string, flags=re.MULTILINE+re.VERBOSE)

    # 内部リンク・ファイルの除去 
    # 除去対象：[[記事名]]、[[記事名|表示文字]]、[[記事名#節名|表示文字]]、[[ファイル:Wi.png|thumb|説明文]]
    replaced = re.sub(r'\[\[(?:    [^|]*?    \|)*?(  (?!Category:)  ([^|]*?))\]\]', r'\1', replaced, flags=re.MULTILINE+re.VERBOSE)

    # Template:Langの除去 
    # 除去対象：{{lang|言語タグ|文字列}}
    replaced = re.sub(r'\{\{lang(?:    [^|]*?    \|)*?([^|]*?)\}\}', r'\1', replaced, flags=re.MULTILINE+re.VERBOSE)

    # 外部リンクの除去
    # 除去対象[http(s)://xxxx] 、[http(s)://xxx xxx]
    replaced = re.sub(r'\[https?://(?:    [^\s]*?    \s)?([^]]*?)\]', r'\1', replaced, flags=re.MULTILINE+re.VERBOSE)

    # HTMLタグの除去
    # 除去対象 <xx> </xx> <xx/>
    replaced = re.sub(r'<.+?>', '', replaced, flags=re.MULTILINE+re.VERBOSE)
#flags プログラムに与えるべき引数をコマンドラインから自動的に解析して取り出したり、指定されてなかったときにデフォルト値を定義できたり便利
    return replaced
for i, (key, value) in enumerate(patt.items()):#enumerate forループの中でリスト（配列）などのイテラブルオブジェクトの要素と同時にインデックス番号（カウント、順番）を取得できる。今回はマークアップ削除した物を順番を変えないでそのままの列順に並べてあげる
#items(): 各要素のキーkeyと値valueに対してforループ処理
    replaced = rem_mark(value)
    patt[key] = replaced
#リクエスト作成
#APIを取得する為のサンプルコードほぼ丸パクリしてきた
S = requests.Session()
URL = "https://commons.wikimedia.org/w/api.php"
PARAMS = {
#requestsでリクエストした際のリクエスト情報、詳細、パラメーター、ステータスみたいな物

    "action": "query",#どこの行を動かすか　jsonfile
    "format": "json",#jsonファイル読み込み
    "titles": "File:" + patt['国旗画像'],#国旗画像　取得したい対象のファイルを指定
    "prop": "imageinfo",#APIのimageinfoを呼び出す、ファイル参照をURLに変換する
    "iiprop":"url"#URLに変換
}
R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']
for k, v in PAGES.items():#ファイル参照された物を、urlに変化してそれのデータとページを取得、指定する。
    print (v['imageinfo'][0]['url'])
#\1~9一致した文字列の１～９番目に対応する文字列に置換します。
#\{\{lang     '{{lang'(マークアップ開始)
#(?:          キャプチャ対象外のグループ開始
#    [^|]*?   '|'以外の文字が0文字以上、非貪欲
#    \|       '|'
#)*?          グループ終了、このグループが0以上出現、非貪欲
#([^|]*?)     キャプチャ対象、'|'以外が0文字以上、非貪欲(表示対象の文字列)
#\}\}         '}}'(マークアップ終了)
#\[https?://  '[http://'(マークアップ開始)
#(?:            キャプチャ対象外のグループ開始
#    [^\s]*?  空白以外の文字が0文字以上、非貪欲
#    \s       空白
#)?           グループ終了、このグループが0か1出現
#([^]]*?)     キャプチャ対象、']'以外が0文字以上、非貪欲（表示対象の文字列）
#\]           ']'(マークアップの終了)
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
#\[\[              '[['(マークアップ開始)
#(?:               キャプチャ対象外のグループ開始
#    [^|]*?        '|'以外の文字0文字以上、非貪欲
#    \|            '|'
#)*?               グループ終了、このグループが0以上出現、非貪欲(No27との変更点)
#(                 グループ開始、キャプチャ対象
#  (?!Category:)   否定の先読(含んだ場合は対象外としている)
#  ([^|]*?)     '|'以外が0文字以上、非貪欲(表示対象の文字列)
#)
#\]\]         ']]'（マークアップ終了)