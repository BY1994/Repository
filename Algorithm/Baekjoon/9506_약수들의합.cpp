/*
9506 약수들의 합 

수학, 구현, 정수론 

약수구하기 
*/

#include <stdio.h>
#include <math.h>

int divisor[100001];
int d;

int main(void)
{
    int n, sum;
    while (1) {
        scanf("%d", &n);
        if (n == -1) break;
        d = 0; sum = 1;
        for (int i = 2; i <= sqrt(n); ++i) {
            if (n % i == 0) divisor[d++] = i;
        }
        for (int i = d-1; i >= 0; --i) {
            if (n / divisor[i] == divisor[i]) {
                sum += divisor[i];
                continue;
            }
            divisor[d++] = n / divisor[i];
            sum += divisor[d-1] + divisor[i];
        }
        if (sum == n) {
            printf("%d = 1", n);
            for (int i = 0; i < d; ++i) {
                printf(" + %d", divisor[i]);
            }
            printf("\n");
        } else {
            printf("%d is NOT perfect.\n", n);
        }
    } 

    return 0;
}


