/*
1871 좋은 자동차 번호판

구현 
*/
#include <stdio.h>

int n, diff;
char plate_number[9];

int main(void)
{
    scanf("%d", &n);
    for (int tc = 0; tc < n; tc++) {
        scanf("%s", plate_number);
        diff = (plate_number[0] - 'A') * 676 + (plate_number[1] - 'A') * 26 +\
        (plate_number[2] - 'A') - ((plate_number[4] - '0')*1000 + (plate_number[5] - '0')*100 +\
        (plate_number[6]-'0')*10 + (plate_number[7] - '0'));
        if (diff >= -100 && diff <= 100)
            printf("nice\n");
        else
            printf("not nice\n");
    }
    return 0;
}
