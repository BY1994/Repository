"""
1057 토너먼트
"""

N, A, B = map(int, input().split())
if A > B:
    A, B = B, A

ans = 1
while(True):
    if A+1 == B and A % 2 == 1:
        break
    A = (A+1) // 2
    B = (B+1) // 2
    ans += 1

print(ans)



# https://www.acmicpc.net/source/17191734
"""
N,a,b=map(int,input().split())
round=0
a-=1
b-=1
while(a!=b):
    round+=1
    a=a//2
    b=b//2
print(round)
"""

# https://www.acmicpc.net/source/20697448
"""
#include <stdio.h>

int main()
{
	int a,b,n,r=0;
	scanf("%d %d %d",&n,&a,&b);
	while(a!=b){
		r++;
		a= a/2 + a%2;
		b= b/2 + b%2;
	}
	printf("%d",r);
}
"""
