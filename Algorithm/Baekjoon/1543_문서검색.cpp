/*
1543 ���� �˻�

greedy 

���ڿ� �޴� ����� 6503 ������ Ű���忡 ������ ��� ���� 
*/

#include <stdio.h>
#include <string.h> 

char document[2501];
char word[51];

int main(void)
{
	int len_d, len_w;
	int ans = 0;
	scanf("%[^\n]", document);
	getchar();
	scanf("%[^\n]", word);
	getchar();
	len_d = strlen(document);
	len_w = strlen(word);
	
	for (int i = 0; i < len_d;) {
		int flag = 1;
		for (int j = 0; j < len_w; ++j) {
			if (document[i+j] != word[j]) {
				flag = 0;
				break;
			}
		}
		if (flag) i += len_w, ans++;
		else i++;
	}
	printf("%d\n", ans);
	return 0;
}
