

# boj2579
'''
n = 6
l = [10, 20, 15, 25, 10, 20]

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
'''

# boj2193.py
'''
n = 1 >> 1
n = 2 >> 10
n = 3 >> 100, 101
n = 4 >> 1000, 1001, 1010
n = 5 >> 10000, 10001, 10010, 10100, 10101
n = 6 >> 100000, 100001, 100010, 100100, 101000, \
        100101, 101001, 101010
n = 7 >> 1000000, 1000001, 1000010, 1000100, 1001000, 1010000, \
        1000101, 1001001, 1001010, 1010001, 1010010, 1010100, 1010101,
점화식
dp[n] = dp[n-2] + dp[n-1]

n = int(input())
dp = [0, 1, 1]
for i in range(3, 100):
    dp.append(dp[i-1] + dp[i-2])
print(dp[n])
'''


# boj1796.py
'''
1. 왼쪽 오른쪽으로 나눠서 dp를 하면 될거 같음(처음은 무조건 오른쪽만 가겠지만)
2. 1을 어떻게 구현할까 1시간 가량 생각했으니 딱히 방법을 모르겠음..
3. 그래서 다른 사람의 소스를 참조함
'''