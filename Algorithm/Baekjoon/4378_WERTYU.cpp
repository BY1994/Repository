/*
4378 WERTYU

�Է� ũ�Ⱑ �ִ� ������ �˷������ �� ������
���� ���ǿ� �װ� ������.
10������ ������ ����Ѵٰ� �Ѵ�. 
https://www.acmicpc.net/board/view/54751
 
�׽�Ʈ�غ��� ���� ������
https://www.acmicpc.net/board/view/22581
[RP[;E ES;LOMH PM YJR DYTRRY/

https://www.acmicpc.net/board/view/25503
1234567890-=WERTYUIOP[]\SDFGHJKL;'XCVBNM,./
*/

#include <stdio.h>

char first_line[13] = {'`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='};
char second_line[13] = {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'};
char third_line[11] = {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\''};
char fourth_line[10] = {'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'};
char dict[128];
char str[100001];

void init(void){
	for (int i = 1; i < 13; ++i)
		dict[first_line[i]] = first_line[i-1];
	for (int i = 1; i < 13; ++i)
		dict[second_line[i]] = second_line[i-1];
	for (int i = 1; i < 11; ++i)
		dict[third_line[i]] = third_line[i-1];
	for (int i = 1; i < 10; ++i)
		dict[fourth_line[i]] = fourth_line[i-1];
	dict[' '] = ' ';
} 

int main(void) {
	init();
	while (scanf("%[^\n]", str) != EOF) {
		getchar();
		for (int i = 0; str[i]; ++i) str[i] = dict[str[i]];
		printf("%s\n", str);
		for (int i = 0; i < 100001; ++i) str[i] = 0;
	}
	return 0;
}
