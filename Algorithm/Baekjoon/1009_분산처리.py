"""
https://www.acmicpc.net/board/view/78976
놓치기 쉬운 예외 케이스
1
10 2
정답 10
내 출력 0
"""

# 통과
import sys
input = sys.stdin.readline

def check(a, b):
    if b == 1:
        return a % 10
    if b % 2:
        return ((check(a, b//2)**2)*a)%10
    else:
        return ((check(a, b//2)**2))%10

for tc in range(int(input())):
    a, b = map(int, input().split())
    ret = check(a, b)
    if ret == 0:
        print(10)
    else:
        print(ret)

# 1등 풀이
# 동일한 방법인데 while 로 구현
# https://www.acmicpc.net/source/29468629
"""
    while (N--) {
        int a = 0, b = 0, ans = 1; ReadInt(a); ReadInt(b);
        for (; b; b >>= 1) {
            if (b & 1) ans = ans * a % 10;
            a = a * a % 10;
        }
        WriteInt((ans + 9) % 10 + 1); w[i++] = '\n';
    }
"""

# 시간초과
"""
import sys
input = sys.stdin.readline

def check(a, b):
    if b == 1:
        return a % 10
    if b % 2:
        return (check(a, b//2)*check(a, b//2)*a)%10
    else:
        return (check(a, b//2)*check(a, b//2))%10

for tc in range(int(input())):
    a, b = map(int, input().split())
    ret = check(a, b)
    if ret == 0:
        print(10)
    else:
        print(ret)
"""
