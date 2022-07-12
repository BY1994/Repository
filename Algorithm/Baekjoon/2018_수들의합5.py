"""
2018 수들의 합 5

투 포인터

모범 풀이 질문 답변
https://www.acmicpc.net/board/view/94551
답변)
그냥 수학입니다.
a부터 m개의 연속된 자연수들을 더하면 n을 만들 수 있다고 합시다.
그 m개의 자연수들에서 전부 a씩 빼면
0, 1, 2, 3, ..., m-1 이 될 것이고 그 합은 m(m-1)/2 이므로
n = am + m(m-1)/2 입니다.
즉, 어떤 자연수 m을 골랐는데
1부터 m까지의 합을 n에서 뺀 결과가 0 또는 m의 양의 배수이면 됩니다.
위 코드의 i 변수로 m값의 후보를 찾는 것이고 1부터 i까지의 합이 sum입니다.
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
