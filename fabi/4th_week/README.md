# 4주차(2020.05.07 ~ 2020.05.14)
[도둑질](https://programmers.co.kr/learn/courses/30/lessons/42897)

## 해답 찾기 과정
1. 열심히 시도하였으나 시간초과로 실패..
2. 다음에 다시 풀어봐야지

## 소스코드(python3)
```
# pro_dp_snitch.py
def solution(money):
    m = len(money)
    if m <= 3:
        return max(money[0], money[1], money[2])

    def dp(n):
        if n < 0:
            return 0
        if n < 3:
            return money[n]
        return max(money[n] + dp(n-2), money[n-1] + dp(n-3))

    return dp(m-1)

if __name__ == '__main__':
    print(solution([5,9,7,29]))

```