/*
10799 �踷���

stack
���� ���ذ� �ټ� ��ٷο� 
() �� ����� �������̰�, �� �ܴ� �踷����ε�,
�������� ���� ©���� ������� �踷��� ������ ���ϴ� ����
������ ����� stack ���� Ǯ����Ѵٴ� ������ �� ���� �ʴµ�,
������ �־��� �׸��� ���� stack ���� Ǯ �� �ִ� ���� �� �� �ִ�. 
*/

#include <stdio.h> 
char stick[100010];
int sp; // stack ���� index �� �־ �� 
int ans;

int main(void)
{
	scanf("%s", stick);
	for (int i = 0; stick[i];) {
		if (stick[i] == '(') {
			if (stick[i+1] == ')') { // ������ 
				ans += sp;
				i++;
			} else
				sp++;
		} else { // ')'
			ans += 1;
			sp--;
		}
		i++;
	}
	printf("%d\n", ans);
	return 0;
}
