/*
1032 ��� ������Ʈ 

����, ���ڿ� 
*/

#include <stdio.h>
char filename[51][51];
char pattern[51];

int main(void)
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%s", filename[i]);
	}
	// ��ġ�� 
	for (int i = 0; filename[0][i]; ++i) {
		// ���Ϻ� 
		pattern[i] = filename[0][i];
		for (int j = 1; j < n; ++j) {
			if (filename[j][i] != filename[0][i]) {
				pattern[i] = '?';
			}
		}
	}
	printf("%s\n", pattern);
	return 0;
}
