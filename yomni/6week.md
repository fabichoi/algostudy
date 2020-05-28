# 6 week  
[이친수](https://www.acmicpc.net/problem/2193)

## 문제 풀이
1. 1자리 이친수는 1개
2. 2자리 이친수는 1개
3. 다음과 같은 방식으로 아래의 점화식이 성립된다.
>
> 1  
>  
> 1<span style="color:red">0</span>  
>  
> 10<span style="color:red">1</span>  
> 10<span style="color:red">0</span>  
>  
> 
> 101<span style="color:red">0</span>  
> 100<span style="color:red">1</span>  
> 100<span style="color:red">0</span>  

**점화식**

```text
b[i]    = 1 (i = 1 or 2)  
        = b[i - 1] + b[i - 2] (i >= 2)
```

## 소스코드(kotlin)
```kotlin
import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    val N = nextInt();
    var dp = Array<Long>(91, { 0 });
    
    // base case
    dp[0] = 1;
    dp[1] = 1;

    for (i in 2 until N + 1) {
        dp[i] = dp[i - 2] + dp[i - 1];
    }

    println(dp[N - 1]);
}
```

