/*
1453 �ǽù� �˹�

���� 
������� �̹� �ɾƼ� ���߿� ��û�� ����� �������� Ƚ�� ���� 
*/

#include <stdio.h>
int computer[101];

int main(void)
{
    int N; int count = 0; int seat;
    scanf("%d", &N);
    while (N--) {
        scanf("%d", &seat);
        if (computer[seat]) count++;
        else computer[seat] = 1;
    }
    printf("%d\n", count);

    return 0;
}
