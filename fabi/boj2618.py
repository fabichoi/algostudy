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