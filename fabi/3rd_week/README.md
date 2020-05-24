# 3주차(2020.04.30 ~ 2020.05.07)
[경찰차](https://www.acmicpc.net/problem/2618)

## 해답 찾기 과정
1. 이 문제도 결국 다른 사람 소스 참조함..
2. 탐욕법으로는 대충 해결 방안이 생각나는데, dp로는 아직도 잘 모르겠음.
3. 차후에 좀 더 실력이 늘면 다시 풀어봐야 할 것으로 보임.

## 소스코드(python3)
```
# boj2618.py
def dist(a, b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

if __name__ == "__main__":
    n = 6
    w = 3
    c = [
        [1, 1],
        [3, 5],
        [5, 5],
        [2, 3],
        [6, 6]
    ]
    dp = [[-1 for _ in range(1001)] for __ in range(1001)]
    back = [0 for _ in range(1001)]
    choose = [[0 for _ in range(1001)] for __ in range(1001)]

    def solve(x, y):
        here = max(x,y) + 1
        if here == w+2:
            return 0
        if dp[x][y] != -1:
            return dp[x][y]

        return min(solve(here, y) + dist(c[x], c[here]), solve(x, here) + dist(c[y], c[here]))

    solve(0,1)

    print(choose)
```