#include <stdio.h>
#include <string.h>

int palindrome(char* word, int n)
{
	for (int i = 0; i < n/2; i++) {
		if (word[i] != word[n-1-i]) return 0;
	}
	return 1;
}

int main(void)
{
	char word[110];
	scanf("%s", word);
	printf("%d\n", palindrome(word, strlen(word))); 
	return 0;
}
