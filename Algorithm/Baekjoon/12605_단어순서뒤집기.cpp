/*
12605 단어순서 뒤집기 

stack 에 단어를 통째로 넣을 방법이 없어서
시작점과 끝점을 저장했다.

input 을 받을 때 ' ' 공백이 있으면 %s 가 거기서 끊겨버려서
마지막에 '\n' 을 만날 때까지 받도록 하는 방법을 찾았다.
" %[^\n]" 앞에 띄어쓰기를 안 하면 다음 값을 입력 받을 수 없다. 
https://clgnsdl94.tistory.com/m/24 

다른 풀이
(1) 비슷하게 stack 에 인덱스를 저장하는 방식
https://www.acmicpc.net/source/7564505
(2) stack 을 2차원 배열로 해서 아예 글자를 다 넣는 방식
*/
#include <stdio.h>

int N;
char sentence[51];
int sp;
int stack[101];

int main(void)
{
    scanf("%d", &N);
    for (int tc = 1; tc <= N; tc++) {
        int i;
        printf("Case #%d:", tc);
        sp = 0;
        scanf(" %[^\n]", sentence);
        stack[sp++] = 0;
        for (i = 0; sentence[i]; ++i) {
            if (sentence[i] == ' ') {
                stack[sp++] = i;
                stack[sp++] = i+1;
            }
        }
        stack[sp] = i;
        while (sp > 0) {
            printf(" ");
            for (i = stack[sp-1]; i < stack[sp]; ++i) {
                printf("%c", sentence[i]);
            }
            sp -= 2;
        }
        printf("\n");
    }
}
