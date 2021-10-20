"""
3052 나머지
"""
remain = [0] * 1001
ans = 0
for _ in range(10):
    n = int(input())
    remain[n % 42] += 1
    if remain[n % 42] == 1:
        ans += 1
print(ans)


# C++ 풀이
# https://www.acmicpc.net/source/29796983
# 배열에 1로 체크해놓고 배열 돌면서 합 구하기
"""
#import<cstdio>
int a[42],n,s;
main(){while(scanf("%d",&n)>0)a[n%42]=1;for(auto n:a)s+=n;printf("%d",s);}
"""

# Python 풀이
# https://www.acmicpc.net/source/17644522
"""
b = [int(input())%42 for i in range(10)]
print(len(set(b)))
"""
