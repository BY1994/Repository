/*
23375 Arm Coordination

���� �����ϴ� ���� ���� �簢���� �׸��µ�,
���� ��ǥ�� �����ϱ� ������
�����ϸ� ������ ���̸�ŭ ���� �׸� �簢������ ���� �����ϴ� �� ����. 

10^9 ������ ������ int �� ó���Ͽ���. 
*/
#include <stdio.h>

int main(void)
{
    int x, y, r;
    scanf("%d %d", &x, &y);
    scanf("%d", &r);

    printf("%d %d\n", x-r, y-r);
    printf("%d %d\n", x-r, y+r);
    printf("%d %d\n", x+r, y+r);
    printf("%d %d\n", x+r, y-r);

    return 0;
}
