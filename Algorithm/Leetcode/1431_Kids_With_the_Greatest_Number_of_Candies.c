/* 1431 */

#include <malloc.h>

bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize){
	int max = 0;
    bool * ret = (bool *)malloc(candiesSize*4);
    
    for (int i = 0; i < candiesSize; i++) {
    	if (candies[i] > max) max = candies[i];
	}
	
	for (int i = 0; i < candiesSize; i++) {
		if (candies[i] + extraCandies >= max) ret[i] = 1;
		else ret[i] = 0;
    }
    
    *returnSize = candiesSize;
    return ret;
}


