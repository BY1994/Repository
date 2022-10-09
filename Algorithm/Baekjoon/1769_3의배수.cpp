/*
1769 3의 배수 

1000000 자리는 int 범위 안에 들어오지 않지만
그걸 9 * 100만으로 계산하면 바로 int 범위 안에 들어옴
그래서 처음 받은 걸 바로 줄임 

그러나 처음 들어온 인풋이 한 자리수일 경우를 대비하여
예외 처리를 goto 문으로 넣음 
*/
#include <stdio.h>

char numbers[1000010];
int num;
int count;

int main(void)
{
	int i;

	// start
	scanf("%s", numbers);
	for (i = 0; numbers[i]; i++) {
		num += (int)(numbers[i] - '0');
	}
	if (i == 1)
		goto out;
	count++;
	
	// find ans
	while (num / 10) {
		int next = 0;
		while (num){
			next += num % 10;
			num /= 10;
		}
		num = next;
		count++;
	}
	
	// print
out:
	printf("%d\n", count);
	printf("%s\n", (num % 3)? "NO" : "YES");
	return 0;
}
