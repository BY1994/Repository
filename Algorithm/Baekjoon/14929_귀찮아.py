"""
14929 귀찮아

2022.06.10 통과
a1a2 + a1a3 + a2a3 를 구하는 것인데,
a1a2 + a1a3 + a2a1 + a2a3 + a3a1 + a3a2 를 구하고 /2 를 하는 것도 똑같아서 아래와 같이 풀어하였다.
처음에 문제를 잘못 이해해서 위와 같이 구하려다가 꼼수로 /2 만 하면 정답이 나온다는 걸 깨달았다.
a1(a2 + a3) + a2(a1 + a3) + a3 (a1 + a2)
이렇게 묶어보면 배열의 값 하나와 전체 합에서 그 값을 뺀 것의 곱임을 알 수 있다.
(그거빼고 한 번씩 다 곱해보기 때문에)

다른 방식으로는 누적합으로 풀 수도 있다.
a1(a2 + a3) + a2(a3) 이런 식으로 맨 오른쪽부터 앞으로 오면서 하나씩 값이 더 누적되어간다.
그래서 prefix sum 을 구하고, 한칸씩 줄여가면서 곱하면 된다.

다른 사람들이 제출한 풀이를 보니 이걸 더 간단하게 입력을 받으면서 prefix sum 을 만들어두고
그걸 바로 바로 곱해서 더했다.

a1*(0) + a2*(a1) + a3*(a1+a2) + a4*(a1+a2+a3) 
"""

n = int(input())
x = list(map(int, input().split()))

total = sum(x)
ans = 0
for i in range(n):
    ans += x[i]*(total-x[i])

print(ans//2)

# 모범 풀이
"""
#include <iostream>
using namespace std;
int sum, n,x;
long long res;
int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> x;
		res += x * sum;
		sum += x;
	}
	cout << res;
}
"""
