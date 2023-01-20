/*
2391 Sascha (����� ���б�) 

����, ���ڿ�
������ �����ε� �ʹ� �����ϰ� �����ؼ� Ʋ�ȴ�.
replacement �� ��Ģ�� �ְ� �װ� �ּҷ� �ؾ��Ѵٰ� �����ߴµ�,
�������� �� replacement �� single letter ���� �ش��̶�� �κ��� ���� �ٽ� �����ϰ� �����Ͽ���. 
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

// Ʋ�� Ǯ�� 
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
