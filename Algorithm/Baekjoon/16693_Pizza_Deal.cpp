/*
16693 Pizza Deal 

������, ��Ģ����
������ ���� vs. �������� ������ �־����� �� �� �̵��� ���� ����
A1 / P1
R1 * R1 * 3.14 / P2
�� �� ū �� ã�� �Ŵϱ� �Ѵ� P1*P2 �� �����־���.
�׷��� �Ʒ� �ڵ��� ���� ���� 

3.14 �� JPL ���� �༺�� �׹��� ����� �� ����Ѵٴ� ������ ����ߴ�.
(�̰� �۰� ����ϸ� Ʋ���� ���� �����͵��� �ִ�)
 https://kids.donga.com/mobile/?ptype=article&no=20190314154822649351
*/

#include <stdio.h>

int main(void)
{
    double A1, P1, R1, P2;
    scanf("%lf %lf", &A1, &P1);
    scanf("%lf %lf", &R1, &P2);
    
    if (A1 * P2 > R1 * R1 * 3.141592653589793 * P1)
        printf("Slice of pizza\n");
    else printf("Whole pizza\n");

    return 0;
}
