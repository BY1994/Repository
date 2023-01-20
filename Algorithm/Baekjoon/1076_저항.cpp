/*
1076 ���� 

���� 
���� ����� string.h ��� ���߸��� �����ߴµ�,
ä�� �� �˾Ƽ� �߰��Ǿ �°� ä����
 
white �� ���� Ŀ�� �ٸ� ���� ���ϸ� int ������ �Ѿ ������ ����
long long ���� ���� 
*/

#include <stdio.h>
#include <string.h>

struct resistor{
    char *color;
    long long val;
    long long mul;
}resistors[10] = {{"black", 0LL, 1LL}, {"brown", 1LL, 10LL}, {"red", 2LL, 100LL},\
    {"orange", 3LL, 1000LL}, {"yellow", 4LL, 10000LL}, {"green", 5LL, 100000LL},\
    {"blue", 6LL, 1000000LL}, {"violet", 7LL, 10000000LL}, {"grey", 8LL, 100000000LL},\
    {"white", 9LL, 1000000000LL}};

char a[10], b[10], c[10];

int main(void)
{
    long long ans = 0;
    scanf("%s", a);
    scanf("%s", b);
    scanf("%s", c);
    for (int i = 0; i < 10; ++i) {
        if (strcmp(a, resistors[i].color) == 0) {
            ans += resistors[i].val;
            break;
        }
    }
    for (int i = 0; i < 10; ++i) {
        if (strcmp(b, resistors[i].color) == 0) {
            ans = ans * 10 + resistors[i].val;
            break;
        }
    }
    for (int i = 0; i < 10; ++i) {
        if (strcmp(c, resistors[i].color) == 0) {
            ans *= resistors[i].mul;
            break;
        }
    }
    printf("%lld\n", ans);
    return 0;
}
