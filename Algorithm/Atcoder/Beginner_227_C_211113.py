# online c compiler
"""
#include <stdio.h>

int main()
{
    long long N;
    long long ans = 0;
    scanf("%lld", &N);

    for (long long a = 1; a < 4700; a++) {
        for (long long b = a; b < 1000000; b++) {
            if (a * b * b > N) break;
            //("### %lld %lld %lld\n",a, b, N/(a*b) + (b-1));
            ans += N/(a*b) - (b-1);
        }
    }
    printf("%lld\n", ans);

    return 0;
}

"""
