/*
1075 ������

brute force
������ ���� 2�ڸ��� ����Ž���ϸ� �ǹǷ�
100 ���� ���� �ȴ�! 
(2,000,000,000 �� �� �ʿ� ����)
https://www.acmicpc.net/board/view/17326

������ �׷��� �� Ǯ�� ���� ����� ����� ���� �� �� �� �����ָ�
���� �� ���� �� ���Ƽ� �������� Ǯ����. 
*/

#include <stdio.h>

int main(void)
{
    long long N, F;
    scanf("%lld", &N);
    scanf("%lld", &F);
    
    N -= N % 100;
    if (N % F)
        printf("%02lld\n", ((N/F)*F + F) % 100);
    else
        printf("00\n");

    return 0;
}
