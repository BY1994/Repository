/*
1049 기타줄

greedy

처음엔 낱개로 사는 거 / 패키지로 사는거 / 패키지로 삼고 %6한 거 낱개로 사는 거
3개만 비교하면 된다고 생각했는데 문제 예제가 답이 안 나왔다.
그래서 그냥 브루트 포스로 풀어버렸다.
다시 확인해보니 이전 풀이는 구현에 실수가 있었던 것 같다. 
*/
#include <stdio.h>

int main(void)
{
	const int MAX = 50001;
	int N, M, a, b, left, price;
	int package = MAX;
	int one = MAX;
	int min_money = MAX;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; i++) {
		scanf("%d %d", &a, &b);
		if (package > a) package = a;
		if (one > b) one = b;
	}
	for (int one_num = 0; one_num <= N; one_num++) {
		int package_num = N - one_num;
		left = (package_num % 6)? 1 : 0;
		price = one_num * one + (package_num/6 + left) *package;
		if (min_money > price) min_money = price;
	}
	printf("%d\n", min_money); 
	return 0;
}

// 깔끔한 풀이
//  https://www.acmicpc.net/source/1200553
#if 0
#include<stdio.h>
int n,m,i,p,q,a,b;
int main(){
	scanf("%d%d",&n,&m);
	p=q=9999;
	for(i=0;i<m;i++){
		scanf("%d%d",&a,&b);
		p=p<a?p:a;
		q=q<b?q:b;
	}
	p=p<q*6?p:q*6;
	printf("%d",n/6*p+(n%6*q<p?n%6*q:p));
}
#endif
// https://www.acmicpc.net/source/8763726
/*
import sys
q = lambda: list(map(int,sys.stdin.readline().strip().split()))
n,m = q()
p = []
s = []
for i in range(m):
	t1,t2 = q()
	p.append(t1)
	s.append(t2)
if min(s)*6 > min(p):
	price = min(p) * (n//6)
	if min(s)*(n%6) < min(p):
		price += min(s)*(n%6)
	else:
		price += min(p)
else:
	price = min(s) * n
print(price)
*/
