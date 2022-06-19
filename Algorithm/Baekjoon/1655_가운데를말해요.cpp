/*
1655 가운데를 말해요

selection sort 에 자기 자리를 찾아가는 걸 binary search 로 구현하는 방법
-> 이건 계산해봐야하는데 문제의 시간 제한 안에 아슬아슬하게 못 들어올 지도... 

maxh 과 minh 에 들어간 개수가 1개 이하로 차이나도록 이렇게 했는데,
꼭 이렇게 개수 비교하게 안 짜도 한 개씩 번갈아서 들어가게 하고 top 비교해서
교환하는 것만 써줘도 가능하다. 

모범 풀이 참고: https://regularmember.tistory.com/142
priority queue 사용법: https://breakcoding.tistory.com/123
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
