/*
2391 Sascha (사샤의 글읽기) 

구현, 문자열
간단한 문제인데 너무 복잡하게 생각해서 틀렸다.
replacement 에 규칙이 있고 그걸 최소로 해야한다고 생각했는데,
문제에서 각 replacement 는 single letter 마다 해당이라는 부분을 보고 다시 간결하게 수정하였다. 
*/

#if 1
#include <stdio.h>

char target[129];
char cand[10001][129];

int main(void)
{
    int tc, n, ans, count, min;
    scanf("%d", &tc);
    while (tc--) {
        min = 129;
        scanf("%s", target);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            count = 0;
            scanf("%s", cand[i]);
            for (int j = 0; target[j]; ++j) {
                if (target[j] != cand[i][j]) count++;
            }
            if (min > count) {
                min = count;
                ans = i;
            }
        }
        printf("%s\n", cand[ans]);
    }
    return 0;
}
#endif

// 틀린 풀이 
#if 0
#include <stdio.h>

char target[129];
char cand[10001][129];

int main(void)
{
    int tc, n, ans, count, min;
    scanf("%d", &tc);
    while (tc--) {
        min = 129;
        scanf("%s", target);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            char dict[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z'};
            count = 0;

            scanf("%s", cand[i]);
            for (int j = 0; target[j]; ++j) {
                if (dict[target[j]-'a'] == cand[i][j]) continue;
                count++;
                dict[target[j]-'a'] = cand[i][j];
            }
            if (min > count) {
                min = count;
                ans = i;
            }
        }
        printf("%s\n", cand[ans]);
    }
    return 0;
}
#endif
