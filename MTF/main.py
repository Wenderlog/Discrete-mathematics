def mtf(s, a):
    res = []
    for i in s:
        res.append(a[i])
        for k in a.keys():
            a[k] += (1 if a[k] < a[i] else 0)
        a[i] = 0
    return res

a = {'a': 0, 'b': 1, 'c': 2}
print(*mtf('baccaaabaaacccbbbbb', a), sep='')

def reverse_mtf(s, a):
    res = ''
    for i in s:
        res += a[int(i)]
        a = [a[int(i)]] + a[:int(i)] + a[int(i) + 1:]
    return res

a = ['a', 'b', 'c']
print(reverse_mtf('1120100210020020000', a) == 'baccaaabaaacccbbbbb')


