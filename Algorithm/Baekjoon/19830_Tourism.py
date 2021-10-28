"""
19830 Tourism

최대로 방문하는 두 경로를 찾도록 해서
문자열 찾기 처럼 어려운 문제처럼 보이지만
문자열과 달리 1과 0으로만 들어와서
생각해보면 중간에 공통되는 부분이 젤 많이 겹쳐야
두 경로가 max를 포함할 수 있다.
그러면 앞이랑 뒤만 맞춰주면 된다. 중간을 최대한 공통으로 하게
앞이랑 뒤가 1로 맞던지 0으로 맞던지 하는 걸 찾으면 된다.
"""

char = input()
n = len(char)
s = 0
e = 0
for i in range(n):
    if char[i] == char[-1]:
        s = i
        break

for i in range(n-1, -1, -1):
    if char[i] == char[0]:
        e = i
        break

if n-1 - s > e:
    print(s+1, n-1, s+2, n)
else:
    print(1, e, 2, e+1)



# 같은 풀이인데 계산이 좀 더 압축적
# https://www.acmicpc.net/source/22532198
"""
#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int mn[2], mx[2];
string s;

int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);
	cin >> s;
	for(int i=0;i<s.size();i++) mx[s[i] - '0'] = i+1;
	for(int i=s.size()-1;i>=0;i--) mn[s[i] - '0'] = i+1;

	int f = mx[1] - mn[1] > mx[0] - mn[0];
	cout << mn[f] << " " << mx[f] - 1 << " " << mn[f] + 1 << " " << mx[f];
}
"""
