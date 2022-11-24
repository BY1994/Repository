/*
1919 애너그램 만들기

구현
애너그램 형태를 보자마자 count 배열이 필요하다는 생각이 들었다. 
*/

#include <stdio.h>

int count1[26];
int count2[26];
char word[1001];
inline int abs(int x) {
    return x > 0? x : -x;
}
int main(void)
{
    int ans = 0;

    scanf("%s", word);
    for (int i = 0; word[i]; ++i) {
        count1[word[i]-'a']++;
    }
    scanf("%s", word);
    for (int i = 0; word[i]; ++i) {
        count2[word[i]-'a']++;
    }
    
    for (int i = 0; i < 26; ++i) {
        ans += abs(count2[i] - count1[i]);
    }
    printf("%d\n", ans);

    return 0;
}
