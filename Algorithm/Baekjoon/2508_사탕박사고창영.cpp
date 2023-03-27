/*
2508 사탕 박사 고창영 

구현
가로 세로가 겹친 입력은 주어지지 않는다. 
candy를 tc 마다 초기화 해야하는데, 안 하는 실수 있었음 
*/

#include <stdio.h>
char box[401][401];
int t, r, c;

int main(void)
{
    scanf("%d", &t);
    while (t--) {
        int candy = 0;
        getchar();
        scanf("%d %d", &r, &c);
        for (int i = 0; i < r; ++i)
            scanf("%s", box[i]);
        
        // 1. horizontal
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c-2; ++j) {
                if (box[i][j] == 62 && box[i][j+1] == 111 && box[i][j+2] == 60) candy++;
            }
        }
        // 2. vertical
        for (int j = 0; j < c; ++j) {
            for (int i = 0; i < r-2; ++i) {
                if (box[i][j] == 118 && box[i+1][j] == 111 && box[i+2][j] == 94) candy++;
            }
        }
        printf("%d\n", candy);
    }
    return 0;
}


