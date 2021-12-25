"""
1300 K번째 수
"""

def check(n):
    global N        
    res = 0
    for i in range(1, N+1):
        if n > N*i:
            res += N
        else:
            res += n // i
    return res


def binary_search(n):
    global N
    ans = 0
    left = 1
    right = N*N
    mid = 0

    while left<=right:
        mid = (left+right)//2
        result = check(mid)
        result2 = check(mid-1)
        if result >= n and n > result2:
            return mid
        elif result < n:
            left = mid+1
        else:
            right = mid - 1
    return 0

N = int(input())
k = int(input())

print(binary_search(k))

# 상위 풀이도 비슷한 아이디어
# https://www.acmicpc.net/source/18050023
"""
#include <cstdio>
#define min(a, b)a<b?a:b

int main()
{
    int n, k, left=1, right, i;
    scanf("%d %d", &n, &k);
    right=k;
    while(left<=right){
        int mid=(left+right)/2, cnt=0;
        for(i=1; i*i<=mid; i++)
            cnt+=min(mid/i, n);
        cnt=cnt*2-(i-1)*(i-1);
        if(cnt<k) left=mid+1;
        else right=mid-1;
    }
    printf("%d", left);
    return 0;
}
"""

# 똑같은 수가 여러번 있을 때 정확한 위치를 못 파악
"""
def check(n):
    global N        
    res = 0
    for i in range(1, N+1):
        if n > N*i:
            res += N
        else:
            res += n // i
    return res

def binary_search(n):
    global N
    ans = 0
    left = 1
    right = N*N
    mid = 0

    while left<=right:
        mid = (left+right)//2
        result = check(mid)
        print("### mid", mid, "### result", result)
        if result == n:
            return mid
        elif result < n:
            left = mid+1
        else:
            right = mid - 1
    return 0

N = int(input())
k = int(input())

print(binary_search(k))
"""
