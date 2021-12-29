"""
2003 수들의 합 2
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
p1 = 0
p2 = 1

while (True):
    if p2 > N: break
    s = sum(A[p1:p2])
    if s == M:
        ans += 1
        p2 += 1
    elif s > M:
        if p1+1 == p2:
            p1 += 1
            p2 += 1
        else:
            p1 += 1
    else:
        p2 += 1

print(ans)

# https://www.acmicpc.net/source/31083845
"""
#include<stdio.h>
int main(){
    int N,M,A[10000],c,i,j;
    scanf("%d %d",&N,&M);
    for(c=i=j=0;i<N;c+=!M,i++){
        scanf("%d",A+i);
        for(M-=A[i];M<0;M+=A[j++]);
    }
    printf("%d",c);
}
"""
