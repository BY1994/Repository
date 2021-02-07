
/* 1108: 100% */
#include <malloc.h>

char * defangIPaddr(char * address){
    int dotnum = 0, addrSize, i, j;
    // . ������ �� �ʿ�� ������... => IPv4�� .�� ������ 3���� 
    for (i = 0, addrSize = 0; address[i]; i++, addrSize++) {
        if (address[i] == '.') dotnum++;
    }
    char * ret = (char *) malloc(addrSize + dotnum*3);
    
    for (i = 0, j = 0; address[i]; i++){
        if (address[i] == '.') {
            ret[j++] = '[';
            ret[j++] = '.';
            ret[j++] = ']';
        }
        else ret[j++] = address[i];
    }
    ret[j] = 0;
    return ret;
}


