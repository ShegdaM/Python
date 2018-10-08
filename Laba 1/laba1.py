from math import sqrt

print('Hello world')

def f1(a, b):
    if a < 0 or b < 0:
        raise Exception('You should enter two positive digits.')
    if a % b == 0:
        return True
    else:
        return False
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(f1(a, b))

def f2(m, n):
    if n < m:
        raise Exception('NoSimpleDigits')
    tmp = set(range(2, n))
    for i in range(2, int(sqrt(n))):
        if i in tmp:
            tmp -= set(range(2 * i, n, i))
    return tmp
m = int(input('Enter start: '))
n = int(input('Enter end: '))
print(f2(m, n))

res =[]
def f3(lst):
    for i in lst:
        if type(i) == list:
            f(i)
        else:
            res.append(i)
    return res
lst = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
print(f3(lst))

f = open('out.txt', 'w')
lst = ['first ', 'ht432t ', 'someshit ']
for i in lst:
    f.write(i)
f.close()
