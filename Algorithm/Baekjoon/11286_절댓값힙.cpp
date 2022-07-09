/*
힙

비교를 위한 operator 직접 짜는 법
https://hydroponicglass.tistory.com/169
operator 2개 비교할 때 간단 버전
https://codingdog.tistory.com/entry/c-priority-queue-%EC%98%88%EC%A0%9C-compare-%EA%B5%AC%EC%A1%B0%EC%B2%B4%EB%A7%8C-%EC%9E%98-%EC%A0%95%EC%9D%98%ED%95%A9%EC%8B%9C%EB%8B%A4 
& 넣으니까 적용됨. & 넣은 operator 버전
https://www.geeksforgeeks.org/priority-queue-of-pairs-in-c-with-ordering-by-first-and-second-element/
내 답은 20 ms 인데, 8 ms 보면 PQ 에 값 하나만 넣고,
operator 써서 관리한다. 내 코드처럼 PQ 에 pair 로 관리할 필요 없다.
https://www.acmicpc.net/source/44014284
operator 의 > 와 < 가 내 생각과 반대였음!!!
*/

#include <stdio.h>
#include <math.h>
#include <vector>
#include <queue>
using namespace std;

int N, x;
struct compare{
	bool operator()(pair<int, int> &a, pair<int, int> &b){
		if (a.first != b.first)
			return a.first > b.first;
		return a.second > b.second; 
	}
};
priority_queue<pair<int, int>, vector<pair<int, int> >, compare> PQ;
int main(void)
{
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &x);
		if (x) {
			PQ.push(make_pair(abs(x), x));
		} else{
			if (!PQ.empty()) {
				x = PQ.top().second;
				PQ.pop();
			}
			printf("%d\n", x);
		}
	}
	return 0;
}

/*
compare 직접 짠 복잡 버전
struct compare{
	bool operator()(pair<int, int>a, pair<int, int>b){
		if (a.first < b.first)
			return true;
		else if (a.first > b.first)
			return false;
		else {
			if (a.second <= b.second)
				return true;
			else if (a.second > b.second)
				return false;
		}			
	} 
};
 
*/
