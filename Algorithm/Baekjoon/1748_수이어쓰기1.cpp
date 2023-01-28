/*
1748 수 이어 쓰기 1 

구현 

제일 긴 숫자는 100,000,000 으로 9자리
9자리의 수가 100,000,000 개면, 900000000 이고
8자리의 수가 10,000,000 개이므로 987654321 이런 식으로 될 것
그래서 long long 안에 충분히 들어온다고 판단했다. 

시간 제한이 0.15 초이므로 일일히 써보라는 문제는 아닐 것 
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
