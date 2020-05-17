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
