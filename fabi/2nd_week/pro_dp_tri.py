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
