/*
1526 ���� ū �ݹμ�

brute force
�׸��𽺷��� Ǯ�̸� ���ø��ٰ�
���� ������ ũ�� �ʾƼ�
���� ���� Ǯ�̴� brute force ��� ���� ������ 
*/

#include <stdio.h>

int main(void)
{
    int N, temp, flag;
    scanf("%d", &N);
    for (int i = N; i > 0; --i) {
        temp = i, flag = 1;
        while (temp) {
            if (temp % 10 != 4 && temp % 10 != 7) {
                flag = 0;
                break;
            }
            temp /= 10;
        }
        if (flag) {
            printf("%d\n", i);
            break;
        }
    }

    return 0;
}
