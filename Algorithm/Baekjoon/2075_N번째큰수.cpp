/*
2075 N번째 큰 수

우선순위 큐 

메모리 제한이 12MB 이기 때문에
모든 정보를 다 저장해서 정렬하거나 큐에 넣을 순 없다. 
큐를 최소한의 개수로 유지하도록 구현하였다. 
(역량 테스트 B형 아이디어 스타일과 비슷한 듯) 

처음에 작은 거부터 큰 순서로 정렬해야하는 줄 알았는데,
제일 큰 거부터 거꾸로 N 번째를 구하는 거였다. 
구현하고 나서 예제가 안 나와서 알았지만 다행히 고치기는 매우 쉬웠다.
큐 뒤집을 땐 -만 붙이면 되기 때문에....
*/

#include <stdio.h>
#include <queue>
using namespace std;

int main()
{
    int N, temp;
    priority_queue<int> q;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &temp);
        q.push(-temp);
    }
    for (int i = 1; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &temp);
            if (-q.top() < temp) {
                q.pop();
                q.push(-temp);
            }
        }
    }
    printf("%d\n", -q.top());
    return 0;
}
