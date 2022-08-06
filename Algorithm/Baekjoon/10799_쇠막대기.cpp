/*
10799 쇠막대기

stack
문제 이해가 다소 까다로움 
() 이 모양은 레이저이고, 그 외는 쇠막대기인데,
레이저로 인해 짤려서 만들어진 쇠막대기 조각을 구하는 문제
지문만 보고는 stack 으로 풀어야한다는 생각이 잘 들지 않는데,
지문에 주어진 그림을 보면 stack 으로 풀 수 있는 것을 알 수 있다. 
*/

#include <stdio.h> 
char stick[100010];
int sp; // stack 없이 index 만 있어도 됨 
int ans;

int main(void)
{
	scanf("%s", stick);
	for (int i = 0; stick[i];) {
		if (stick[i] == '(') {
			if (stick[i+1] == ')') { // 레이저 
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
