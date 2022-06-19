/*
1655 ����� ���ؿ�

selection sort �� �ڱ� �ڸ��� ã�ư��� �� binary search �� �����ϴ� ���
-> �̰� ����غ����ϴµ� ������ �ð� ���� �ȿ� �ƽ��ƽ��ϰ� �� ���� ����... 

maxh �� minh �� �� ������ 1�� ���Ϸ� ���̳����� �̷��� �ߴµ�,
�� �̷��� ���� ���ϰ� �� ¥�� �� ���� �����Ƽ� ���� �ϰ� top ���ؼ�
��ȯ�ϴ� �͸� ���൵ �����ϴ�. 

��� Ǯ�� ����: https://regularmember.tistory.com/142
priority queue ����: https://breakcoding.tistory.com/123
*/

#include <stdio.h>
#include <queue>
using namespace std;

priority_queue<int, vector<int> > maxh;
priority_queue<int, vector<int>, greater<int> > minh;

int main(void)
{
	int N, num;
	int maxnum = 0;
	int minnum = 0; 
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d", &num);
		if (maxnum <= minnum) {
			maxh.push(num);
			maxnum++;
		} else{
			minh.push(num);
			minnum++;
		}
		if (!minh.empty()){
			int maxtop = maxh.top();
			int mintop = minh.top();
			if (maxtop > mintop) {
				maxh.pop();
				minh.pop();
				maxh.push(mintop);
				minh.push(maxtop);
			}
		}
		printf("%d\n", maxh.top());
	}
	return 0;
}
