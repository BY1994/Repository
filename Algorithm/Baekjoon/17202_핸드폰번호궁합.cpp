/*
17202 �ڵ��� ��ȣ ���� 

���̳��� ���α׷������� �з��Ǿ��־ Ǭ ����
�ܼ� ���� ��������. 

���� ���� 1 �� �Է� �� �ٷ� �߸� �޾Ҵµ�... �׷��� ���� ���Դ�;; 
*/

#include <stdio.h>

int array[17];

int main(void) {
	for (int i = 0; i < 16; i += 2) scanf("%1d", &array[i]);
	for (int i = 1; i < 16; i += 2) scanf("%1d", &array[i]);
	for (int i = 16; i > 2; --i) {
		for (int j = 0; j < i-1; ++j) {
			array[j] = (array[j] + array[j+1]) % 10;
		}
	}
	printf("%d%d\n", array[0], array[1]);
	return 0;
}
