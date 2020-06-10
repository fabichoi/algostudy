# 8주차(2020.06.05 ~ 2020.06.11)
[계단 오르기](https://www.acmicpc.net/problem/2579)

## 해답 찾기 과정 [계단 오르기]
1. 책에 있는 해설을 참고하고 풀음.
2. 해설 참고하기 전에 드는 생각은.. 뭔가 +1, +2 이렇게 해서 step을 더해주는거였던걸로 기억났는데
3. 결국 어떻게 푸는지 모르겠어서 해설 보고 풀음.
4. 해설을 보니 생각보다 간단한데,
- 1,2번째 계단은 초기값을 넣어주고
- 현재 위치(3번째 계단 이상)부터는 
    1. 바로 전계단을 밟고 올라오는 경우
    2. 바로 전계단은 안밟고 올라오는 경우
- 로 나뉠수 있다.
- 1의 case에서는 현재 계단(i)과 바로 전계단(i-1), 그리고 전전전계단의 누적 최대값(ac_max(i-3))을 더하면 되고
- 2의 case에서는 현재 계단(i)과 전전계단의 누적 최대값(ac_max(i-2))을 더하면 된다.
- 1,2의 최대값을 누적 최대값 배열에 집어넣고 n이 될때 까지 loop를 돌리면 된다.

## 소스코드(python3) [계단 오르기]
```
# boj2579.py

def solve(n, l):
    s = [0 for _ in range(n+1)]
    l = [0] + l

    if n == 1:
        return l[1]

    if n == 2:
        return l[1] + l[2]

    s[1] = l[1]
    s[2] = l[1] + l[2]

    for j in range(3, n+1):
        noJump = l[j] + l[j-1] + s[j-3]
        jump = l[j] + s[j-2]

        if noJump > jump:
            s[j] = noJump
        else:
            s[j] = jump

    return s[n]

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

print(solve(n, l))

```