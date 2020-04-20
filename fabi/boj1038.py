from itertools import combinations
n = int(input())
a = list(range(0,10))
res = []
for i in range(1, 11):
    combi = list(combinations(a, i))
    for c in combi:
        c = list(c)
        c.sort(reverse=True)
        res.append(''.join(map(str,c)))
res = list(map(int, res))
res.sort()
if n > 1022:
    print(-1)
else:
    print(res[n])