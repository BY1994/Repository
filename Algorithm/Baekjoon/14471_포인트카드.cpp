/*
14471 ����Ʈ ī��

�׸���

M-1 �� �̻��� ��ǰ�� �����ٴ� ������ �־
���� ������ �ƴ϶� �׸��� ������ ��!!
�� �κ��� �ű��ߴ�. 
*/
#include <stdio.h>
#define max(a, b) ((a) > (b))? (a) : (b)

int main(void)
{
    int N, M, A, B, need;
    int total = 0, m = 0;
    scanf("%d %d", &N, &M);
    while (M--) {
        scanf("%d %d", &A, &B);
        need = max(N-A, 0);
        total += need;
        m = max(need, m);
    }
    printf("%d\n", total - m);

    return 0;
}
