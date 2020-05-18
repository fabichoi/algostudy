'''
balls = [i for i in range(300001)]
tri = [0]
tetra = [0]
n = 15

# 각 사면체당 대포알 갯수 구하기
for i in range(1, 122):
    tri.append(tri[-1] + i)
    tetra.append(tri[-1] + tetra[-1])

# n이 300000 까지 구하기
li = [0 for _ in range(200)]
d = [0 for _ in range(300001)]
for i in range(1,200):
    li[i] = i * (i+1) * (i+2) // 6
n = int(input())
for i in range(1, n+1):
    if li[i] > n:
        break
    for j in range(li[i], n+1):
        if i > 1:
            d[j] = min(d[j-li[i]] + 1, d[j])
        elif i == 1:
            d[j] = d[j - li[i]] + 1
print(d[n])
'''


li = [0 for _ in range(200)]
d = [0 for _ in range(300001)]
for i in range(1,200):
    li[i] = i * (i+1) * (i+2) // 6
n = int(input())
for i in range(1, n+1):
    if li[i] > n:
        break
    for j in range(li[i], n+1):
        if i > 1:
            d[j] = min(d[j-li[i]] + 1, d[j])
        elif i == 1:
            d[j] = d[j - li[i]] + 1
print(d[n])
