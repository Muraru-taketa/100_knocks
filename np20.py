import json
#sysで読み込まなくてもいいいので直接ファイルを読みこむことにする。
with open("jawiki-country.json") as f:#wikiからイギリスをピックアップする。
    unk_json = f.readline() #unk_json代入したこの関数で指定したjsonファイルを読み込み
    while unk_json: #jsonファイルが詠み込まれたとき以下を実行する。
        unk_dict = json.loads(unk_json)
        if unk_dict["title"] == u"イギリス":#イギリスを指定
            print(unk_dict["text"])
        unk_json = f.readline()