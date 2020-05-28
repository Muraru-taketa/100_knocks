#テンプレート.py
x = 12
y = "気温"
z = 22.4

def template(x, y, z):
    return "{0}時の{1}は{2}°".format(x, y, z)#文字を埋め込む;format

print(template(x, y, z))