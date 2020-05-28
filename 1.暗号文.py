def cipher(txt):
#小文字の時はtrueを返して219 -文字コードに変換する:islower
    result = ''
    for s in txt:
        if s.islower():
            result += chr(219 - ord(s))#ord()ユニコード組み込み関数
        else:
            result += s
    return result

#元素記号の英文使いますね。
target = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
#元のやつ
print(target)
#暗号化する
result1  = cipher(target)
print('暗号化:' + result1)

#m元に戻すよ
result2 = cipher(result1)
print('復号:' + result2)