/*
1864 문어 숫자 

구현
숫자 
*/

#include <stdio.h>

int str2num[128];
char text[9];

int main(void)
{
    str2num['-'] = 0;
    str2num['\\'] = 1;
    str2num['('] = 2;
    str2num['@'] = 3;
    str2num['?'] = 4;
    str2num['>'] = 5;
    str2num['&'] = 6;
    str2num['%'] = 7;
    str2num['/'] = -1;
    
    while (1) {
        int ans = 0;
        scanf("%s", text);
        if (text[0] == '#') break;
        for (int i = 0; text[i]; i++) {
            ans <<= 3;
            ans += str2num[text[i]];
        }
        printf("%d\n", ans);
    }
    return 0;
}
