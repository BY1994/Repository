/*
1524 세준세비 

구현 시뮬레이션

priority_queue 를 전역으로 선언했다가
초기화가 안 되는 문제가 있었다.
문제에 주어진 예제를 반대로 뒤집으면 발견할 수 있다.
https://www.acmicpc.net/board/view/89755

답변한 게시물
정답이 C가 되는 경우는 없다.
https://www.acmicpc.net/board/view/45193
*/

#include <stdio.h>
#include <queue>
using namespace std;

int main()
{
    int T, N, M;
    long long temp;
    scanf("%d", &T);
    while (T--) {
        priority_queue<long long> S;
        priority_queue<long long> B;

        getchar();
        scanf("%d %d", &N, &M);
        for (int i = 0; i < N; i++) {
            scanf("%lld", &temp);
            S.push(-temp);
        }
        for (int i = 0; i < M; i++) {
            scanf("%lld", &temp);
            B.push(-temp);
        }
        while (1) {
            if (S.empty()) {
                printf("B\n");
                break;
            }
            else if (B.empty()) {
                printf("S\n");
                break;
            }
            if (-S.top() >= -B.top())
                B.pop();
            else
                S.pop();
        }
    }

    return 0;
}
