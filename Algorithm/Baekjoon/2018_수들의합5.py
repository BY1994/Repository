"""
2018 수들의 합 5

투 포인터
"""

N = int(input())
left = 1
right = 1
cur = 1
ans = 0
while left <= right and right <= N:
    if cur == N:
        ans += 1
        right += 1
        cur += right
    elif cur < N:
        right += 1
        cur += right
    else:
        cur -= left
        left += 1

print(ans)

# 다른 풀이
# https://www.acmicpc.net/source/171292
"""
#include<stdio.h>

int main()
{
	int n,i,cnt=0,sum=0;
	scanf("%d",&n);
	for(i=1;sum<=n;i++){
		sum +=i;
		if((n-sum)>=0 && (n-sum)%i==0) cnt++;
	}
	printf("%d",cnt);
	return 0;
}
"""
