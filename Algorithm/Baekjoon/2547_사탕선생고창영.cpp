/*
2547 ���� ���� ��â��

Ʋ�ȴ� ����
1. unsigned long long ���� �����ϴ���
��� �л����� ������ �� ������ ������ ���
% N �� �Ź� ���ִ� �۾��� �ʿ��ϴ�
https://www.acmicpc.net/board/view/1422

2. �ʱ�ȭ�� Test Case ���� ���־���ϴµ�, �� �� ���� �����.
���� ������ �¾Ƽ� ��û Ʋ�� �Ŀ� �߰��ߴ�. 
�ʱ�ȭ�� �ٽ� �����غ��� ���� ���� �Խñ�
https://www.acmicpc.net/board/view/80377 
*/
#include <stdio.h>

int main()
{
    int T;
    unsigned long long N;
    unsigned long long total;
    unsigned long long candy;
    scanf("%d", &T);
    while (T--) {
        getchar();
        scanf("%llu", &N);
        total = 0;
        for (unsigned long long i = 0; i < N; ++i) {
            scanf("%llu", &candy);
            total += candy;
            total %= N;
        }
        if (total % N) printf("NO\n");
        else printf("YES\n");
    }

    return 0;
}
