/*
1919 �ֳʱ׷� �����

����
�ֳʱ׷� ���¸� ���ڸ��� count �迭�� �ʿ��ϴٴ� ������ �����. 
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
