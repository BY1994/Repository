#include <stdio.h>

int N;
char cmd[6];
int data;
int stack[10001];
int idx;

// instead of strcmp

int main()
{
    scanf("%d", &N);
    for (int i = 0; i<N; i++)
    {
        scanf("%s", cmd);
        if (cmd[0] == 's') printf("%d\n", idx);
        else if (cmd[0] == 'e') printf("%d\n", !idx);
        else if (cmd[0] == 't') printf("%d\n", (idx)?(stack[idx-1]):(-1));
        else if (cmd[0] == 'p')
        {
            if (cmd[1] == 'u')
            {scanf("%d", &data); stack[idx++] = data;}
            else printf("%d\n", (idx)?(stack[--idx]):(-1));
        }
        
    }
    printf("Hello World");

    return 0;
}
