/*
6679 싱기한 네자리 숫자

Brute Force

10진수, 12진수, 16진수로 표현한 자릿수 합이 모두 똑같은 숫자
문제 예제에는 일부만 나와있는데, 전체를 다 출력해야한다.
Text 로 정답 제출해도 인정된다. 
*/

#include <stdio.h>

int add_all(int num, int div) {
	int ret = 0;
	while (num) {
		ret += num % div;
		num /= div;
	}
	return ret;
}

int main(void)
{
	for (int num = 1000; num <= 9999; num++) {
		int num10 = add_all(num, 10);
		int num12 = add_all(num, 12);
		int num16 = add_all(num, 16);
		if (num10 == num12 && num12 == num16) printf("%d\n", num);
	}
	return 0;
}
