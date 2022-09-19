/*
6679 �̱��� ���ڸ� ����

Brute Force

10����, 12����, 16������ ǥ���� �ڸ��� ���� ��� �Ȱ��� ����
���� �������� �Ϻθ� �����ִµ�, ��ü�� �� ����ؾ��Ѵ�.
Text �� ���� �����ص� �����ȴ�. 
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
