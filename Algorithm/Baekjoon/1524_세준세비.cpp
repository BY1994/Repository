/*
1524 ���ؼ��� 

���� �ùķ��̼�

priority_queue �� �������� �����ߴٰ�
�ʱ�ȭ�� �� �Ǵ� ������ �־���.
������ �־��� ������ �ݴ�� �������� �߰��� �� �ִ�.
https://www.acmicpc.net/board/view/89755

�亯�� �Խù�
������ C�� �Ǵ� ���� ����.
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
