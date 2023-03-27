/*
2508 ���� �ڻ� ��â�� 

����
���� ���ΰ� ��ģ �Է��� �־����� �ʴ´�. 
candy�� tc ���� �ʱ�ȭ �ؾ��ϴµ�, �� �ϴ� �Ǽ� �־��� 
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


