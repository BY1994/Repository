"""
10816 숫자 카드 2

이분 탐색
https://velog.io/@madfinger/Binary-Search%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC

시간 단축 방법
(local 변수 사용시 더 빠름)
https://www.acmicpc.net/board/view/68809
https://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function

이분탐색 upper bound / lower bound
https://blog.naver.com/bestmaker0290/220820005454
"""

import sys

def binary_search_upper(n):
    global N
    left = 0#-10000000 
    right = N-1 #10000000
    mid = 0

    while left< right:
        mid = (left+right)//2
        if cards[mid] > n:
            right = mid
        else:
            left = mid + 1
    return right

def binary_search_lower(n):
    global N
    left = 0#-10000000 
    right = N-1 #10000000
    mid = 0

    while left< right:
        mid = (left+right)//2
        if cards[mid] >= n:
            right = mid
        else:
            left = mid + 1
    return right

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
M = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
for i in numbers:
    a = binary_search_upper(i)
    b = binary_search_lower(i)
    #print("###", a, b)
    if cards[b] < i and b < N-1:
        b += 1
    if cards[a] > i and a > 0:
        a -= 1
    if cards[b] == i:
        print(a - b+1, end=" ")
    else:
        print(0, end=" ")

# 메모리 쓰고 개수 세는 방법도
# https://www.acmicpc.net/source/18487883
"""
#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 5e5;
const int INF = 1e7;
typedef long long ll;

int n, m;
int a[INF * 2 + 1];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    int t;
    for (int i = 0; i < n; ++i) {
        cin >> t;
        a[t + INF]++;
    }

    cin >> m;
    for (int j = 0; j < m; ++j) {
        cin >> t;
        cout << a[t + INF] << " ";
    }

    return 0;
}
"""

# 시간초과
"""
import sys

def binary_search_upper(n):
    global N
    ans = -1
    left = 0#-10000000 
    right = N-1 #10000000
    mid = 0

    while left<=right:
        mid = (left+right)//2
        if cards[mid] == n:
            ans = mid
            left = mid + 1
        elif cards[mid] < n: # elif 아니고 if 하면 ==n 일 때 else로 빠져서 문제
            left = mid+1
        else:
            right = mid - 1
    return ans

def binary_search_lower(n):
    global N
    ans = -1
    left = 0#-10000000 
    right = N-1 #10000000
    mid = 0

    while left<=right:
        mid = (left+right)//2
        if cards[mid] == n:
            ans = mid
            right = mid -1
        elif cards[mid] < n:
            left = mid+1
        else:
            right = mid - 1
    return ans

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
M = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
for i in numbers:
    a = binary_search_upper(i)
    b = binary_search_lower(i)
    if a >= 0:
        print(a - b+1, end=" ")
    else:
        print(0, end=" ")
"""
