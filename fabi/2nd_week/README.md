# BOJ 1038 해설

1. 처음에 어떻게 풀어야 할까 계속 혼자 생각하다가

2. 따로 접근법이 안나와서 인터넷에 있는 해설을 참고함.

3. 가장 큰 힌트는 입력이 1023 이상 나올수가 없음.

4. 왜냐면 감소하는 수열의 가장 큰 값은 9876543210 이기 때문

   > 0,1,2,3,4,5,6,7,8,9의 10개의 숫자 중 1개를 뽑는 방법은 10가지 * 2 (9개 뽑는 경우도 동일)
   >
   > 2개뽑는 방법은 10C2 = 10! / (2! * 8!) = 10 * 9 / 2 = 45 가지 * 2 (8개 뽑는 경우도 동일)
   >
   > 3개뽑는 방법은 10C3 = 10! / (3! * 7!) = 10 * 9 * 8 / 6 = 120 가지 * 2 (7개 뽑는 경우도 동일) 
   >
   > 4개뽑는 방법은 10C4 = 10! / (4! * 6!) = 10 * 9 * 8 * 7 / 24 = 210 가지 * 2 (6개 뽑는 경우도 동일) 
   >
   > 5개뽑는 방법은 10C5 = 10! / (5! * 5!) = 10 * 9 * 8 * 7 * 6 / 120 = 252
   >
   > 마지막으로 10개를 뽑는 방법은 1
   >
   > 위를 모두 더하면 1023이 됨(20 + 90 + 240 + 420 + 252 + 1)
   >
   > 그러나 0부터 시작하므로 실제 index는 0 ~ 1022이 됨

5. python3에서는 combination 을 기본적으로 사용할 수 있어서 4번의 로직을 다 구한 뒤
6. 숫자를 오름차순으로 정렬해서 list에 저장하고
7. list의 index를 그대로 출력하게 하면 되며
8. 1023이상일 경우 -1을 출력하도록 로직 구성하면 완료.