/*
17566 Bus Logic

��Ʈ����ŷ

���� ���� ���� ���ذ� �����
ù��° ������ Ʋ�� ����:
(1) ������� (m) �� bus stop �� ������ �ƿ� �ش� ��θ� �� ���� ����
(2) �������� ���� ����̱� ������ (������ �׸�) ����� ����� �� �����ؾ��� 
*/
#include <stdio.h>
int m, b, s;
int count;
char stop[51];
unsigned long long stops[51];
unsigned long long max;

int main(void)
{
	scanf("%d %d %d", &m, &b, &s);
	for (int i = 0; i < b; ++i) {
		scanf("%s", stop);
		if (stop[m-1] == '0') continue; // Ʋ�� ����: bus stop ���� �� ���ܸ� �� �� 
		for (int j = 0; j < s; ++j) {
			if (j == m-1) continue; // Ʋ�� ����: �������� ���ϱ� ����� ����� �� ���� 
			if (stop[j] == '1') stops[i] |= 1LL;
			stops[i] <<= 1LL;
		}
		max |= stops[i];
	}
	for (int j = 0; j < s; ++j) {
		if (max & 1LL) count++;
		max >>= 1LL;
	}
	printf("%d\n", count);
	return 0;
}

