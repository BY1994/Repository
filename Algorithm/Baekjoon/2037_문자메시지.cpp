/*
2037 ���ڸ޽���

����
 
%d ���� �� \n �� �־��ָ� ���ڿ� ���� �κп� \n ���� ���´�. 
button[text[i-1]] ��� ����ϴµ� ó���� text[i-1] �� ������� ���� ��̴�.  
if elseif �� �ϱ� �Ⱦ �迭�� ��� ���̺��� �������. 
*/

#include <stdio.h>
#include <string.h>

char text[1001];
char button[128];
char push[128];

void init_buttons(void)
{
    button['A'] = button['B'] = button['C'] = 1;
    button['D'] = button['E'] = button['F'] = 2;
    button['G'] = button['H'] = button['I'] = 3;
    button['J'] = button['K'] = button['L'] = 4;
    button['M'] = button['N'] = button['O'] = 5;
    button['P'] = button['Q'] = button['R'] = button['S'] = 6;
    button['T'] = button['U'] = button['V'] = 7;
    button['W'] = button['X'] = button['Y'] = button['Z'] = 8;

    push['A'] = push['D'] = push['G'] = push['J'] = push['M'] = push['P'] = push['T'] = push['W'] = 1;
    push['B'] = push['E'] = push['H'] = push['K'] = push['N'] = push['Q'] = push['U'] = push['X'] = 2;
    push['C'] = push['F'] = push['I'] = push['L'] = push['O'] = push['R'] = push['V'] = push['Y'] = 3;
    push['S'] = push['Z'] = 4;
    push[' '] = 1;
}

int main(void)
{
    int p, w;
    int total_time = 0;
    scanf("%d %d\n", &p, &w);
    scanf("%[^n]", text);
    init_buttons();
    total_time += push[text[0]]*p;
    for (int i = 1; i < strlen(text); ++i) {
        if (button[text[i-1]] && (button[text[i-1]] == button[text[i]])){
            total_time += w;
        }
        total_time += push[text[i]]*p;
    }
    printf("%d\n", total_time);
    return 0;
}
