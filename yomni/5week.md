# 5 week  
[캡틴 이다솜](https://www.acmicpc.net/problem/1660)

## 문제 풀이
1. 사면체의 대포알 갯수 합 배열을 구한다.(대포알 갯수의 합은 주어지는 N 보다 클 수 없다.)
2. Knapsack 동전교환 알고리듬과 동일하게 동작  
화폐체계 : 사면체의 대포알 개수 합  
거스름돈 : N


**점화식**

```text
// 한변의 길이가 i인 사면체의 대포알의 총 갯수
b[i] = b[i - 1] + n(n + 1) / 2

// N개를 만들 때 최소 사면체 갯수
dp[j] = min(dp[j], dp[j - b[i]] + 1)
i는 1 부터 (사면체의 대포알 개수 합 === 화폐 종류 수) 까지  
j는 1부터 N + 1 까지
```

## 소스코드(kotlin)
```kotlin
import java.lang.Integer.min
import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    val N = nextInt();
    var b = Array<Int>(N + 2, { 0 });
    var dp = Array<Int>(N + 2, { 0 });
    var cnt = 1;

    b[0] = 0;
    for (i in 1..Int.MAX_VALUE) {

        if (b[i - 1] + ((i * (i + 1)) / 2) > N) {
            break;
        }
        b[i] = b[i - 1] + ((i * (i + 1)) / 2);
        cnt++;
    }

    for (i in 0 until N + 1) {
        dp[i] = i;
    }

    for (i in 1 until cnt + 1) {
        for (j in 1 until N + 1) {
            if (j - b[i] >= 0) {
                dp[j] = min(dp[j], dp[j - b[i]] + 1);
            }
        }
    }

    println(dp[N]);
}
```

