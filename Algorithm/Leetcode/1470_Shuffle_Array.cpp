#include <malloc.h>

/*
numsSize�� 2n, n�� �迭�� ���� ũ���� �� ����
heap buffer overflow ��
*/

/* // ���� �õ� ���� �ַ�� (16 ms)
int* shuffle(int* nums, int numsSize, int n, int* returnSize) {
	int * returns = (int *)malloc(sizeof(int)*numsSize);

	for (int i = 0; i < n; i++) {
		returns[i*2] = nums[i];
		returns[i*2+1] = nums[i + n];
	}

	*returnSize = numsSize;
	return returns;
}
*/

// Discussion ���� ���� (12 ms)
int* shuffle(int* nums, int numsSize, int n, int* returnSize) {
	int * returns = (int *)malloc(sizeof(int)*numsSize);

	for (int i = 0, j = 0; i < n; i++, j+=2) {
		returns[j] = nums[i];
		returns[j + 1] = nums[i + n];
	}

	*returnSize = numsSize;
	return returns;
}

// ���ϱ� ������ �ֺ���? 12 ms
int* shuffle(int* nums, int numsSize, int n, int* returnSize) {
	int * returns = (int *)malloc(sizeof(int)*numsSize);
	int j;

	for (int i = 0; i < n; i++) {
		j = i * 2;
		returns[j] = nums[i];
		returns[j + 1] = nums[i + n];
	}

	*returnSize = numsSize;
	return returns;
}

