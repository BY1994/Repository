/*
2857 FBI

���ڿ� ���� 

���� ���� Ʋ�ȴ� ����: 
FBI ���� ������ 3�� ���� ���ƾ��Ѵٰ� �����ؼ�,
i < len - 3 ������ ���� ���Ҵµ�,  
i �� ���� ����ϴ� �Ű�, i+1, i+2 �� �߰��� ����ϴ� �Ŵϱ�
len - 2 �� �´�. 

���� Ʋ�ȴ� ����: 
��� �̸��� FBIFBI �� ��� 2�� ���
https://www.acmicpc.net/board/view/2242
*/

#include <stdio.h>

char name[11];
int len;

int strlen(char *ptr) {
	int count = 0;
	while (*ptr++) count++;
	return count;
}

int main(void)
{
	int flag = 1;
	for (int id = 1; id <= 5; ++id) {
		scanf("%s", name);
		len = strlen(name);
		for (int i = 0; i < len-2; ++i) {
			if (name[i] == 'F' && name[i+1] == 'B' && name[i+2] == 'I') {
				printf("%d ", id);
				flag = 0;
				break;
			}
		}
	}
	if (flag) printf("HE GOT AWAY!\n");
	else printf("\n");

	return 0;
}
