"""
19858 Gold bars (Russian)

1 2 2
2 3 3
2 3 4
2 2 4

1 숫자와 2숫자의 갭이 3숫자보다 큰 경우가 있으면 어떡하지 했는데
그런 경우는 있을 수가 없다.
3숫자가 이미 2숫자보다 값이 크기 때문에 그 갭만큼을 가지고 있다.
그러니까 3숫자가 나눠주면 된다.



1 1 1 하면 -1
2 2 2 하면 3 / 1 1
2 2 4 하면 0

그러나 풀이의 증명 방법을 모르겠다

"""

numbers = list(map(int, input().split()))
index = [1, 2, 3]

numbers = list(zip(numbers, index))
numbers.sort()

diff = numbers[1][0] - numbers[0][0]
half = numbers[2][0] - diff
if numbers[0][0] + numbers[1][0] == numbers[2][0]:
    print(0)
elif half % 2:
    print(-1)
else:
    half = half // 2
    print(numbers[2][1])
    print(half + diff, half)
    

# 최대값도 최소값을 찾을 때 이런 방법을?!
# https://www.acmicpc.net/source/22532298
"""
#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int a[3];

int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);
	for(int i=0;i<3;i++) cin >> a[i];

	int m = (a[0] + a[1] + a[2]) / 2;
	
	int k = max_element(a, a+3) - a, n = min_element(a, a+3) - a, l = 0;
	while(l == k || l == n) l++;

	if(a[k] == m){
		cout << 0;
		return 0;
	}else if(a[k] > m){
		cout << k + 1 << "\n";
		cout << a[k] - m << " " << m;
	}else if(a[k] < m){
		cout << l + 1 << "\n";
		cout << m - a[k] << " " << m - a[n];
	}
}
"""
