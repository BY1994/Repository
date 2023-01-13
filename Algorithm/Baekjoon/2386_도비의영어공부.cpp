/*
2386 도비의 영어 공부 

특정 알파벳이 문장에서 몇 번 나오는지 count 
*/

#include <stdio.h>

int main(void)
{
    char target;
    while (1) {
        int ans = 0;
        char sentence[251] = {0,};

        scanf("%c", &target);
        getchar();
        if (target == '#') break;
        scanf("%[^\n]", sentence);
        getchar();
        
        for (int i = 0; sentence[i]; ++i) {
            if (sentence[i] == target || sentence[i] == target - 32) ans++;
        }
        printf("%c %d\n", target, ans);
    }

    return 0;
}
