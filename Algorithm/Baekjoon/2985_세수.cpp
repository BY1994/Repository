/*
2985 세 수 

사칙연산, 많은 조건 분기 
*/
#include <stdio.h>

int main(void){
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	if (a+b == c) printf("%d+%d=%d\n", a, b, c);
	else if (a-b == c) printf("%d-%d=%d\n", a, b, c);
	else if (a*b == c) printf("%d*%d=%d\n", a, b, c);
	else if (a == b*c) printf("%d/%d=%d\n", a, b, c);
	else if (a == b+c) printf("%d=%d+%d\n", a, b, c);
	else if (a == b-c) printf("%d=%d-%d\n", a, b, c);
	else if (a == b*c) printf("%d=%d*%d\n", a, b, c);
	else if (a*c == b) printf("%d=%d/%d\n", a, b, c);
	return 0;
}
