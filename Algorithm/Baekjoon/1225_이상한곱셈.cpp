/*
1225 �̻��� ����

���ڸ��� ���̱� ������ char �� �޾ƾ���
A: 9 �� ����, B: 9�� ������
81 * �� �� * ���� �̹Ƿ� 81���̰�, long long �ȿ� ���� 
*/

#include <stdio.h>

char A[10001];
char B[10001];

int main()
{
    unsigned long long ans = 0;
    scanf("%s %s", A, B);
    for (int i = 0; A[i]; i++) {
        for (int j = 0; B[j]; j++) {
            ans += (A[i] - '0') * (B[j] - '0');
        }
    }
    printf("%llu\n", ans);

    return 0;
}
