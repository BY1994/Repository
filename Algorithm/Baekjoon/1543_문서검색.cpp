/*
1543 문서 검색

greedy 

문자열 받는 방법은 6503 망가진 키보드에 정리한 방법 참고 
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
