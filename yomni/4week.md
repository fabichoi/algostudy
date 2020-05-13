# 4 week  
[도둑질](https://programmers.co.kr/learn/courses/30/lessons/42897)

## 문제 풀이
마을이 원형으로 이어져 있기 때문에 경우를 두 가지로 나눌 수 있다.
- 첫 집을 무조건 털고, 마지막 집은 털지 않으면서, 최대합
- 첫 집은 건너 뛰고, 마지막 집은 무조건 털면서, 최대합


**점화식**

```text
dp[i] = max(dp[i - 1], money[i] + dp[i - 2])
```

## 소스코드(java)
```java
class Solution {
    public int solution(int[] money) {
        int answer = 0;
        int length = money.length;
        // 첫 집을 무조건 터는 경우의 배열
        int[] dp = new int[length - 1];
        // 마지막 집을 무조건 터는 경우의 배열
        int[] dp2 = new int[length];
        
        // base case
        // 첫 집을 털었으므로, 3번째 집부터 시작
        dp[0] = money[0];
        dp[1] = money[0];
        // 마지막 집을 털었으므로, 첫 집은 못털고, 두번째 집은 터는 경우
        dp2[0] = 0;
        dp2[1] = money[1];

        for(int i = 2; i < length - 1; i++){
            dp[i] = Math.max(dp[i - 2] + money[i], dp[i - 1]);
        }

        for(int i = 2; i < length; i++){
            dp2[i] = Math.max(dp2[i - 2] + money[i], dp2[i - 1]);
        }
        
        return Math.max(dp[length - 2], dp2[length - 1]);
    }
}
```
