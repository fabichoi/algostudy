# 2주차(2020.04.23 ~ 2020.04.30)
[정수 삼각형](https://programmers.co.kr/learn/courses/30/lessons/43105)

## 해답 찾기 과정
1. 어디서 많이 본 문제였음
2. 찾아보니 '알고리즘 문제해결 전략' 책에 있어서 참고함
3. 한칸씩 내려가면서 cache중에 큰 값과 삼각형의 값을 합산하여 구하면 됨
4. 실제 구현한 코드에서는 cache의 내용이 n-1줄에서 부터 들어가서 0,0에 최대값이 나오도록 수행됨
> 예제 기준으로 다음과 같은 cache가 만들어짐
> 30
> 23, 21
> 20, 13, 10
> 7, 12, 10, 10

## 소스코드(python3)
```
# pro_dp_tri.py
def solution(triangle):
    n = len(triangle)
    cache = [[-1 for _ in range(i+1)] for i in range(n+1)]

    def dp(y, x):
        if y == n-1:
            return triangle[y][x]
        if cache[y][x] != -1:
            return cache[y][x]
        cache[y][x] = max(dp(y+1, x), dp(y+1, x+1)) + triangle[y][x]
        return cache[y][x]

    return dp(0, 0)

if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
```