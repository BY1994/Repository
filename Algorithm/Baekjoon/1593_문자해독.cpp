#include <stdio.h>

char W[3010];
char S[3000010];
#define MAX_ARRAY 58
int myalpha[MAX_ARRAY];
int testalpha[MAX_ARRAY];

int check(int *a, int *b) {
    for (int i = 0; i < MAX_ARRAY; i++) {
        if (a[i] != b[i]) return 0;
    }
    return 1;
}

int main(void)
{
    int g, s;
    int ans = 0;
    scanf("%d %d", &g, &s);
    scanf("%s", W);
    scanf("%s", S);

    for (int i = 0; i<g; i++) {
        myalpha[W[i]-'A'] += 1;
        testalpha[S[i]-'A'] += 1;
    }

    ans += check(myalpha, testalpha);
    
    for (int i = 0; i<s-g; i++) {
        testalpha[S[i]-'A'] -= 1;
        testalpha[S[i+g]-'A'] += 1;
        ans += check(myalpha, testalpha);
    }

    printf("%d\n", ans);

    return 0;
}

// 풀이 비슷
// https://www.acmicpc.net/source/34265114
