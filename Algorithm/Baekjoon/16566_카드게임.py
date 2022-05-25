"""
16566 카드 게임

Binary Search upper bound: https://awesomeroo.tistory.com/31

사용한 카드를 버려야하기 때문에 (아래 풀이는 운 좋게 통과했지만...)
사용한 카드들의 연속된 구간들이 다음 구간의 가장 큰 카드를 가리키게 해야한다.
구간이 합쳐질 수 있으니 연속 구간을 그룹으로 관리해야한다.
DisjointSet
https://lastknight00.tistory.com/52
"""

N, M, K = map(int, input().split())
minsu = list(map(int, input().split()))
chulsu = list(map(int, input().split()))
minsu.sort()
possible = [0]*M

for i in range(K):
    # 이분 탐색
    left = 0
    right = M-1
    while left < right:
        mid = (left + right)//2
        if minsu[mid] == chulsu[i]:
            left = mid+1
        elif minsu[mid] < chulsu[i]:
            left = mid+1
        elif minsu[mid] > chulsu[i]:
            right = mid

    while possible[right] == 1:
        right += 1
    print(minsu[right])
    possible[right] = 1

# DisjointSet 모범 풀이
# https://lastknight00.tistory.com/52
"""
#include <iostream>
#include <algorithm>
using namespace std;
int n,m,k,d[4000000], e[4000001], i;
int f (int a) {
    return a == e[a]? e[a]: e[a]=f(e[a]);
}
void u(int a, int b){
    e[f(a)] = e[f(b)];
}
int main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> n >> m >> k;
    for(; i < m; i++) cin >> d[i];
    for (i = 1; i <= n; i++) e[i] = i;
    sort(d, d+m);
    while(k--) {
        cin >> i;
        n = f(upper_bound(d, d+m, i) - d);
        cout << d[n] << "\n";
        u(n, n+1);
    }
}
"""
