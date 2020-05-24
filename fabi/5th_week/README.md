# 5주차(2020.05.15 ~ 2020.05.22)
[캡틴 이다솜](https://www.acmicpc.net/problem/1660)

## 해답 찾기 과정
1. 이것도 역시 시간초과.. 다른 사람 소스를 참조했는데도 불구하고!
2. 로직이 틀리지는 않았으나, python의 특성상 list 접근하는게 다른 언어보다 좀 느린듯 함
3. append를 이용해서 다시 풀어봐야함.

## 소스코드(python3)
```
# boj1660.py
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
```