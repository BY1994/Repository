#include <stdio.h>
#include <string.h>

char S[1000001];
char bomb[37];
int b_size;
char stack[1000001];
int sp;

int is_bomb(int cur_sp)
{
    if (cur_sp < b_size)
        return 0;
    if (strncmp(&stack[cur_sp - b_size], bomb, b_size))
        return 0;
    return 1;
}

int main(void)
{
    scanf("%s", S);
    scanf("%s", bomb);
    b_size = strlen(bomb);
    
    for (int i = 0; S[i]; ++i) {
        stack[sp++] = S[i];
        if (is_bomb(sp))
            sp -= b_size;
    }
    
    stack[sp] = 0;
    if (sp)
        printf("%s\n", stack);
    else
        printf("FRULA\n");
    return 0;
}