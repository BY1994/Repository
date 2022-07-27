/*
2504 괄호의 값

스택 연습

스택을 2개를 써서 풀었지만,
다른 풀이를 보니 스택은 괄호만 저장하는 1개만 쓰고도 풀 수 있었다.
https://www.acmicpc.net/source/42225762

2022.07.27 통과는 했으나 질문게시판에서 반례를 발견
https://www.acmicpc.net/board/view/95954
([())] 
답이 0이어야하나, bracket 개수만 세도록 코드를 짰기 때문에 2가 출력
*/
#include <stdio.h>

char S[31];
int bracket1, bracket2;
int num_stack[31];
int op_stack[31];
int num_sp, op_sp;

int cal(void)
{
    for (int i = 0; S[i]; ++i) {
        if (S[i] == '(') {
            op_stack[op_sp++] = S[i];
            bracket1++;
        }
        else if (S[i] == '[') {
            op_stack[op_sp++] = S[i];
            bracket2++;
        }
        else if (S[i] == ')') {
            int temp = 0;
            while (op_sp >= 1 && op_stack[op_sp-1] != '(') {
                temp += num_stack[num_sp-1];
                num_sp--;
                op_sp--;
            }
            if (temp == 0)
                num_stack[num_sp++] = 2;
            else
                num_stack[num_sp++] = temp*2;
            op_stack[op_sp-1] = 1;
            bracket1--;
        }
        else if (S[i] == ']') {
            int temp = 0;
            while (op_sp >= 1 && op_stack[op_sp-1] != '[') {
                temp += num_stack[num_sp-1];
                num_sp--;
                op_sp--;
            }
            if (temp == 0)
                num_stack[num_sp++] = 3;
            else
                num_stack[num_sp++] = temp*3;
            op_stack[op_sp-1] = 1;
            bracket2--;
        }

        if (bracket1 < 0) return 0;
        if (bracket2 < 0) return 0;
    }

    if (bracket1 != 0) return 0;
    if (bracket2 != 0) return 0;
    
    while (num_sp > 1) {
        num_stack[0] += num_stack[num_sp-1];
        num_sp--;
    }
    return num_stack[0];
}

int main(void)
{
    scanf("%s", S);

    printf("%d\n", cal());
    return 0;
}