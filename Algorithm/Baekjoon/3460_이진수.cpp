/*
3460 ������ 

����, ���� 
TC ������ �־����� ������
������ 1���� �ִ��� �ݵ�� 2�� �̻� �־ ��!
�� ���������� \n ���߷Ⱦ���. 
*/

#include <stdio.h>

int main(void)
{
    int T, n, bit;
    scanf("%d", &T);
    while (T--) {
        bit = 0;
        scanf("%d", &n);
        while (n) {
            if (n & 1) printf("%d ", bit);
            n >>= 1;
            bit++;
        }
        printf("\n");
    }

    return 0;
}
