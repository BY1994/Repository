/*
17252 ����� �� 

���� or brute force

3�� �ŵ������� �ѹ����� ���� ������ �Ǵ� 
Ʋ�Ƚ��ϴ� => 0 �� ������� ����
0 �� 3�� �ŵ��������� ���� �� ���� ������ NO �� ���;��� 

�ݷ� ã��
https://www.acmicpc.net/board/view/39961 
�ִ� �� 2147483647 �� ������ Runtime Exceed
���� ���� ����� �ذ�� 
*/

#include <stdio.h>
int main(void)
{
	int N;
	int flag = 0;
	scanf("%d", &N);
	while (N) {
		flag = 1;
		if (N % 3 == 2) {
			flag = 0;
			break;
		}
		N /= 3;
	}
	if (flag) printf("YES\n");
	else printf("NO\n");
	return 0;
}
