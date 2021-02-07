/* 1512: 100% */
int numIdenticalPairs(int* nums, int numsSize){
    int ret = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i+1; j < numsSize; j++) {
            if (nums[i] == nums[j]) ret++;
        }
    }
    return ret;
}

/*
이런 풀이도 가능함 
(이 풀이의 단점은 매번 100 배열을 다 돌아야한다는 것) 
(1) 빈도수 계산해서 넣고 
int count[101] = {0};
(2) nC2 = n(n-1)/2; 혹은 문제를 잘 보면 3+2+1 이런 식으로 계산됨 
1이 4개면 첫번째 1이 더해지는 건 3개,
두번째 1이 더해지는 건 2개, 
이렇게 바로 개수를 더해서 넣을 수 있음 
*/
