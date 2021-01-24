
/* HEAP Buffer overflow  => malloc(numsSize) �ؼ� ������
malloc(numsSize * 4) �� �ذ�!
*/

#include <malloc.h>

int* runningSum(int* nums, int numsSize, int* returnSize) {
	int * returns = (int *)malloc(sizeof(int)*numsSize);
	returns[0] = nums[0];
	// ������ ����
	for (int i = 1; i < numsSize; i++)
		returns[i] = returns[i-1] + nums[i];
	*returnSize = numsSize;
	return returns;
}