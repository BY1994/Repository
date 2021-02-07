/* 1672 */
int maximumWealth(int** accounts, int accountsSize, int* accountsColSize){
    int temp, max = 0;
    for (int i = 0; i < accountsSize; i++) {
        temp = 0;
        for (int j = 0; j < accountsColSize[i]; j++) {
            temp += accounts[i][j];
        }
        if (temp > max) max = temp;
    }
    return max;
}

