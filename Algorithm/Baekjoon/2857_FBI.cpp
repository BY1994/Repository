/*
2857 FBI

문자열 연습 

문제 예제 틀렸던 이유: 
FBI 글자 개수인 3개 전에 돌아야한다고 생각해서,
i < len - 3 까지만 포문 돌았는데,  
i 는 원래 사용하는 거고, i+1, i+2 를 추가로 사용하는 거니까
len - 2 가 맞다. 

제출 틀렸던 이유: 
요원 이름이 FBIFBI 인 경우 2번 출력
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
