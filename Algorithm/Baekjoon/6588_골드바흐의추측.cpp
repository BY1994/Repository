/*
6588 �������� ���� 

�����佺�׳׽��� ü���� �Ǽ��� �־���.
���� ���� ����� 100���� �Ǳ⸸ �ϸ� �ȴٰ� �����ߴµ�
i = 1000, j = 2 �� �� ���� ���� ����� 2000 �ۿ� �� �ȴ�.
�� ������ ���� ����� 100���� �� ������ ���ƾ��Ѵ�! 

�ݷ�
999370
0
Ȥ��
1000000
0
https://www.acmicpc.net/board/view/87525 
*/

// ���� �ڵ�
#include <stdio.h>

int prime[1000001];
int main(void)
{
    int n;
    for (int i = 2; i < 500001; ++i) {
        for (int j = 2; i*j < 1000001; ++j) {
            prime[i*j] = 1;
        }
    }
    prime[0] = prime[1] = 1;
    
    while (1) {
        scanf("%d", &n);
        if (n == 0) break;
        for (int i = 2; i <= n/2+1; ++i) {
            if (prime[i] == 0 && prime[n-i] == 0) {
                printf("%d = %d + %d\n", n, i, n-i);
                break;
            }
        }
    }

    return 0;
}

// Ʋ�� �ڵ� 
#if 0
#include <stdio.h>

int prime[1000001];
int main(void)
{
    int n;
    for (int i = 2; i < 1001; ++i) {
        for (int j = 2; j < 1001; ++j) {
            prime[i*j] = 1;
        }
    }
    prime[0] = prime[1] = 1;
    
    while (1) {
        scanf("%d", &n);
        if (n == 0) break;
        // ���� �ݵ�� �����ϹǷ� 1�� �Ѿ�� �Ѿ�� ���� ����
		// 5 / 2 = 2 �̹Ƿ� �߰� ������ 3���� �����Ϸ��� +1�� �ʿ��ߴ�. 
		// ����� �Ϸ��� n/2 + n%2 �� ���� �� 
        for (int i = 2; i <= n/2+1; ++i) {
            if (prime[i] == 0 && prime[n-i] == 0) {
                printf("%d = %d + %d\n", n, i, n-i);
                break;
            }
        }
    }

    return 0;
}
#endif
