/*
1748 �� �̾� ���� 1 

���� 

���� �� ���ڴ� 100,000,000 ���� 9�ڸ�
9�ڸ��� ���� 100,000,000 ����, 900000000 �̰�
8�ڸ��� ���� 10,000,000 ���̹Ƿ� 987654321 �̷� ������ �� ��
�׷��� long long �ȿ� ����� ���´ٰ� �Ǵ��ߴ�. 

�ð� ������ 0.15 ���̹Ƿ� ������ �Ẹ��� ������ �ƴ� �� 
*/

#include <stdio.h>

int main(void)
{
    long long N;
    long long prev = 0LL;
    long long cur = 10LL;
    long long count = 0LL;
    long long len = 1;

    scanf("%lld", &N);
    while (N / cur) {
        count += (cur - prev) * len;
        len++;
        prev = cur;
        cur *= 10LL;
    }
    count += (N-prev+1) * len - 1;
    printf("%lld\n", count);

    return 0;
}
