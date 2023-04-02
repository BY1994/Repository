/*
4388 �޾ƿø� 

����, ����, ��Ģ����
======================
2023.03.29 Ʋ�Ƚ��ϴ� (�޾ƿø� ����� �Ź� ���ع����� ���� �޾ƿø� ����� �����) 
2023.04.02 �¾ҽ��ϴ� 
*/

// �޾ƿø��� ���� ���� �ʰ� carry ������ ���� ��
// (carry �ʱ�ȭ�� �� �ؼ� �� �� Ʋ��) 
#include <stdio.h>

int main(void)
{
    long long a, b, carry;
    int count;
    while (1) {
        scanf("%lld %lld", &a, &b);
        count = 0; carry = 0;
        if (a == 0 && b == 0) return 0;
        while ((a > 0) || (b > 0)) {
            if (a % 10 + b % 10 + carry >= 10) {
                carry = 1;
                count++;
            } else carry = 0;
            a /= 10; b /= 10;
        }
        printf("%d\n", count);
    }

    return 0;
}

// Ʋ�� �ڵ�
// a += 10; �� �ؼ� ���� ���ڰ� ���� �޾ƿø��� �Ǿ���� ���� �ִ�.
// 10 �� �Ǿ������ �޾ƿø��� �� ���Ǵ� ���� 

#if 0
#include <stdio.h>

int main(void)
{
    long long a, b;
    int count;
    while (1) {
        scanf("%lld %lld", &a, &b);
        count = 0;
        if (a == 0 && b == 0) return 0;
        while (a > 0 || b > 0) {
            if (a % 10 + b % 10 >= 10) {
                a += 10;
                count++;
            }
            a /= 10; b /= 10;
        }
        printf("%d\n", count);
    }

    return 0;
}
#endif
