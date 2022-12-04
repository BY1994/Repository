/*
1380 �Ͱ���

���ڿ� 

2022.11.26

fgets �� ���� => ����ʰ�
�ʱ�ȭ ���� scanf("%[^\n]") �� ���� => Ʋ�Ƚ��ϴ� 
status 0 �ʱ�ȭ �߰� => Ʋ�Ƚ��ϴ� 

��� Ʋ�ȴ� ������ �̸� ��� �ڿ� ���͸� ���� �ʾұ� ���� 
*/

#include <stdio.h>

char name[101][61];
int status[101];

int main(void)
{
	int n, id;
	char letter;
	for (int tc = 1; ; tc++) {
		// �̸� �ޱ�
		scanf("%d", &n);
		if (n == 0) break;
		getchar();
		for (int i = 1; i <= n; ++i) {
			for (int j = 0; j < 61; ++j) name[i][j] = 0;
			scanf("%[^\n]", name[i]);
			getchar();
		}
		// �Ͱ��� �м� & ��ȯ
		for (int i = 1; i < 2*n; ++i) {
			scanf("%d %c", &id, &letter);
			if (status[id]) status[id]--;
			else status[id]++;
			getchar();
		}
		// ó������ ���� �Ͱ��� ã��
		for (int i = 1; i <= n; ++i) {
			if (status[i]) {
				printf("%d %s\n", tc, name[i]);
				status[i] = 0;
				break;
			}
		}
	}
	
	return 0;
}

// ����ʰ�
#if 0
#include <stdio.h>

char name[101][61];
int status[101];

int main(void)
{
	int n, id;
	char letter;
	for (int tc = 1; ; tc++) {
		// �̸� �ޱ�
		scanf("%d", &n);
		if (n == 0) break;
		getchar();
		for (int i = 1; i <= n; ++i) {
			fgets(name[i], 61, stdin);
			//scanf("%[^\n]", name[i]);
			//getchar();
		}
		// �Ͱ��� �м� & ��ȯ
		for (int i = 1; i < 2*n; ++i) {
			scanf("%d %c\n", &id, &letter);
			//getchar();
			if (status[id]) status[id]--;
			else status[id]++;
		}
		// ó������ ���� �Ͱ��� ã��
		for (int i = 1; i <= n; ++i) {
			if (status[i]) {
				printf("%d %s", tc, name[i]);
				break;
			}
		}
	}
	
	return 0;
}
#endif
