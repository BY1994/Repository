#include <malloc.h>

/*
numsSize는 2n, n이 배열의 절반 크기라는 걸 몰라서
heap buffer overflow 남
*/

/* // 최초 시도 느린 솔루션 (16 ms)
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

// Discussion 보고 수정 (12 ms)
int* shuffle(int* nums, int numsSize, int n, int* returnSize) {
	int * returns = (int *)malloc(sizeof(int)*numsSize);

	for (int i = 0, j = 0; i < n; i++, j+=2) {
		returns[j] = nums[i];
		returns[j + 1] = nums[i + n];
	}

	*returnSize = numsSize;
	return returns;
}

// 곱하기 변수로 둬보면? 12 ms
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

