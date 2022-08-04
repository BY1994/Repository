/*
15815 천재 수학자 성필

후위표현식 연습
stack

질문 게시글을 보다가 의문을 갖지 않았던 것을 깨달았다
숫자가 한자리수만 들어오는 것인지
https://www.acmicpc.net/board/view/74635
 
반례 만들기
후위 표현식을 고려하지 않고, 문제 예제만 맞는 코드 
(두 예시 다 숫자를 stack 으로, 연산자는 queue 로 구현함) 
https://www.acmicpc.net/board/view/70954
https://www.acmicpc.net/board/view/94263 
입력) 123*+4+
정답) 11 

2022.08.04 통과 
*/
#include <stdio.h>

int stack[110];
int sp;
char formula[110];

int main(void)
{
    scanf("%s", formula);
    for (int i = 0; formula[i]; ++i) {
        if (formula[i] == '+') {
            stack[sp-2] = stack[sp-2] + stack[sp-1];
            sp--;
        }
        else if (formula[i] == '-') {
            stack[sp-2] = stack[sp-2] - stack[sp-1];
            sp--;
        }
        else if (formula[i] == '*') {
            stack[sp-2] = stack[sp-2] * stack[sp-1];
            sp--;
        }
        else if (formula[i] == '/') {
            stack[sp-2] = stack[sp-2] / stack[sp-1];
            sp--;
        } else {
            stack[sp++] = formula[i] - '0';
        }
    }
    printf("%d\n", stack[0]);
    return 0;
}
