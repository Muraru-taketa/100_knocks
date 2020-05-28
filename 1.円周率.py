#円周率.py
txt = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantnm mechanics."
result = []
#文章を単語に分ける
words = txt.split(' ')#区切り文字で分割split
#単語の数だけ出力
for word in words:
	count = 0
	for char in word:#charはよく使ってたから文字列型のやつ 

		#単語の文字を数える
		if char.isalpha():#全ての文字が英字なら真、そうでなければ偽の判定 isalpha
			count += 1
	result.append(count)#append:リストの末尾に要素を加える今回は文字をcountでカウント（数かぞえ）する
print(result)