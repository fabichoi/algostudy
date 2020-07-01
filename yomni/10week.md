# 10 week  
[파일 합치기](https://www.acmicpc.net/problem/11066)

## 문제 풀이
1. 


**점화식**

```text
dp[i][j] : i ~ j 까지의 최소 비용
dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] : 합친 값 중 최소 값을 선택, k는 i와 j의 사이값을 모두 확인해야 한다.
dp[i][j] += sum[j] - sum[j - 1] (i부터 j까지의 합 추가로 더해줘야 함)
```

## 소스코드(kotlin)
```kotlin
import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.min
import java.util.*

fun main(args: Array<String>) {
    val br= BufferedReader(InputStreamReader(System.`in`));

    repeat(br.readLine()!!.toInt()){
        val n=br.readLine()!!.toInt();
        val arr=br.readLine()!!.split(" ").map { it.toInt() }.toIntArray();
        val dp=Array(n){IntArray(n)};
        val sum=IntArray(n);
        sum[0]=arr[0];
        for(i in 1 until n)  sum[i]=sum[i-1]+arr[i];

        for(j in 1 until n){
            for(i in j-1 downTo 0){
                dp[i][j]=987654321;
                for(k in i until j){
                    dp[i][j]= min(dp[i][j],dp[i][k]+dp[k+1][j]);
                }
                if(i!=0)    dp[i][j]+=sum[j]-sum[i-1];
                else    dp[i][j]+=sum[j];
            }
        }
        println(dp[0][n-1]);
    }
}
```

