f = open('a.txt', 'r')
f1 = open('b1.txt', 'w')
f2 = open('b2.txt', 'w')
i = 0
for item in f:
    if i % 2 == 0:
        f1.write(item.upper())
    else:
        f2.write(item.lower())
    i += 1
f.close()
f1.close()
f2.close()
