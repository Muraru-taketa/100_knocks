#集合.py
def n_gram(txt, n):

    result = []
    for i in range(0, len(txt) - n + 1):
        result.append(txt[i:i + n])

    return result

#足し算、掛け算、引き算
# 集合
set_x = set(n_gram('paraparaparadise', 2))
print('X:' + str(set_x))
set_y = set(n_gram('paragraph', 2))
print('Y:' + str(set_y))

# 和
set_wa = set_x | set_y
print('和集合:' + str(set_wa))

# 積集合
set_sk = set_x & set_y
print('積集合:' + str(set_sk))

# 差集合
set_sa = set_x - set_y
print('差集合:' , set_sa)

# 'se'の有無
print('seがXに含まれる:' + str('se' in set_x))
print('seがYに含まれる:' + str('se' in set_y))