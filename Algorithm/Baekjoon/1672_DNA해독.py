"""
1672 DNA 해독

시뮬레이션
"""

N = int(input())
sequence = list(input())
decoding = {'A': {'A':'A', 'G':'C', 'C':'A', 'T':'G'},
            'G': {'A':'C', 'G':'G', 'C':'T', 'T':'A'},
            'C': {'A':'A', 'G':'T', 'C':'C', 'T':'G'},
            'T': {'A':'G', 'G':'A', 'C':'G', 'T':'T'}}
while N > 1:
    sequence[N-2] = decoding[sequence[N-2]][sequence[N-1]]
    N -= 1

print(sequence[0])


# C 언어 코드
# https://www.acmicpc.net/source/24434321
"""
#include <stdio.h>

int main(void){
    int i, N;
    char str[1000001];
    char change[128][128];

    change[(int)'A'][(int)'A']='A';
    change[(int)'A'][(int)'G']='C';
    change[(int)'A'][(int)'C']='A';
    change[(int)'A'][(int)'T']='G';
    change[(int)'G'][(int)'A']='C';
    change[(int)'G'][(int)'G']='G';
    change[(int)'G'][(int)'C']='T';
    change[(int)'G'][(int)'T']='A';
    change[(int)'C'][(int)'A']='A';
    change[(int)'C'][(int)'G']='T';
    change[(int)'C'][(int)'C']='C';
    change[(int)'C'][(int)'T']='G';
    change[(int)'T'][(int)'A']='G';
    change[(int)'T'][(int)'G']='A';
    change[(int)'T'][(int)'C']='G';
    change[(int)'T'][(int)'T']='T';

    scanf("%d %s", &N, str);
    for(i=N-1; i; --i){
        str[i-1]=change[(int)str[i-1]][(int)str[i]];
    }
    printf("%c", str[0]);

    return 0;
}
"""
