/*
5597 ���� �� ���� ��..?

���� ��Ʈ ����
30 �� �� 28 ���� �����Ͽ��� ��, ���� �� �� 2�� ����ϱ� 
*/

#include <stdio.h>

int main()
{
    int n;
    unsigned int check = 0;
    for (int i = 0; i < 28; ++i) {
        scanf("%d", &n);
        check |= (1 << (n-1));
    }

    for (int i = 0; i < 30; ++i) {
        if ((check & 1) == 0) {
            printf("%d\n", i+1);
        }
        check >>= 1;
    }

    return 0;
}
