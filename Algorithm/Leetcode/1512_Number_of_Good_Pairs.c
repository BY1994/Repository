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
�̷� Ǯ�̵� ������ 
(�� Ǯ���� ������ �Ź� 100 �迭�� �� ���ƾ��Ѵٴ� ��) 
(1) �󵵼� ����ؼ� �ְ� 
int count[101] = {0};
(2) nC2 = n(n-1)/2; Ȥ�� ������ �� ���� 3+2+1 �̷� ������ ���� 
1�� 4���� ù��° 1�� �������� �� 3��,
�ι�° 1�� �������� �� 2��, 
�̷��� �ٷ� ������ ���ؼ� ���� �� ���� 
*/
