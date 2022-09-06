/*
1049 ��Ÿ��

greedy

ó���� ������ ��� �� / ��Ű���� ��°� / ��Ű���� ��� %6�� �� ������ ��� ��
3���� ���ϸ� �ȴٰ� �����ߴµ� ���� ������ ���� �� ���Դ�.
�׷��� �׳� ���Ʈ ������ Ǯ����ȴ�.
�ٽ� Ȯ���غ��� ���� Ǯ�̴� ������ �Ǽ��� �־��� �� ����. 
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

// ����� Ǯ��
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
