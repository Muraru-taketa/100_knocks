#パトカー+タクシー2.py　
def  patotaku_pata(pato, taku):

    kougo = "".join(p + t for p,t in zip(pato, taku))
#zipはfor分の中のリスト、pato,takuを同時に扱う、同時に扱うための取り出した物をjoinで文字列を生成する。
    return kougo

print(patotaku_pata("パトカー", "タクシー"))
