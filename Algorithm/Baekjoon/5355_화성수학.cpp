/*
5355 화성 수학 

구현, 사칙연산 
*/

#include <stdio.h>

char op[8];

int main(void)
{
    int T;
    float num;
    scanf("%d", &T);
    while (T--) {
        scanf("%f", &num);
        op[1] = op[2] = op[3] = op[4] = op[5] = op[6] = op[7] = 0;
        scanf("%[^\n]", op);
        for (int i = 0; op[i]; i++) {
            if (op[i] == '@') {
                num *= 3.0;
            } else if (op[i] == '%') {
                num += 5.0;
            } else if (op[i] == '#') {
                num -= 7.0;
            }
        }
        printf("%.2f\n", num);
    }

    return 0;
}
