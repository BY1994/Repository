/*
22864 �Ƿε�

�׸���, �ùķ��̼�
B �ִ밪�� 10,000 �ε� 24�ð� �� ���ص� 240,000 �̹Ƿ�
int ������ ���� �ʴ´�. 
*/

#include <stdio.h>
int main(void)
{
    int A, B, C, M;
    int tired = 0, output = 0;
    scanf("%d %d %d %d", &A, &B, &C, &M);
    for (int h = 0; h < 24; ++h) {
        if (tired + A > M) {
            tired -= C;
            if (tired < 0)
                tired = 0;
        } else {
            tired += A;
            output += B;
        }
    }
    printf("%d\n", output);
    return 0;
}
