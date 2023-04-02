/*
4388 받아올림 

수학, 구현, 사칙연산
======================
2023.03.29 틀렸습니다 (받아올림 결과를 매번 더해버려서 다음 받아올림 결과가 사라짐) 
2023.04.02 맞았습니다 
*/

// 받아올림이 먼저 되지 않게 carry 변수를 따로 뺌
// (carry 초기화를 안 해서 한 번 틀림) 
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

// 틀린 코드
// a += 10; 을 해서 위의 숫자가 먼저 받아올림이 되어버릴 수도 있다.
// 10 이 되어버리면 받아올림이 덜 계산되는 문제 

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
