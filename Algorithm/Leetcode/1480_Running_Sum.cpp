
/* HEAP Buffer overflow  => malloc(numsSize) 해서 오류남
malloc(numsSize * 4) 로 해결!
*/

#include <malloc.h>

int* runningSum(int* nums, int numsSize, int* returnSize) {
	int * returns = (int *)malloc(sizeof(int)*numsSize);
	returns[0] = nums[0];
	// 누적합 저장
	for (int i = 1; i < numsSize; i++)
		returns[i] = returns[i-1] + nums[i];
	*returnSize = numsSize;
	return returns;
}