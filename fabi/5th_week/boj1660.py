li = [0 for _ in range(122)]
d = [i for i in range(300001)]
for i in range(1,122):
    li[i] = i * (i+1) * (i+2) // 6
n = int(input())
for i in range(2, n+1):
    if li[i] > n:
        break
    for j in range(li[i], n+1):
        d[j] = min(d[j-li[i]] + 1, d[j])
print(d[n])
# 문제는 일부 풀리나 시간초과 발생 ㅠㅠ