#replace.py
f = open('x2.txt', 'r')
line = f.readline()

while line:
    print(line.replace("", ''))
    line = f.readline()
f.close()