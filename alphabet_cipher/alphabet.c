#include <stdio.h>

#define SIZE 26

void create_cipher(int cipher[SIZE][SIZE]);
void print_cipher(int cipher[SIZE][SIZE]);

int main(int argc, char **argv)
{
	int cipher[SIZE][SIZE];
	int *keyword, *message;

	/*
	if (argc != 2) {
		printf("Usage: ./cipher <filename>\n");
		return 0;
	}
	*/

	printf("Alphabet Cipher\n");
	printf("a:%d\n",('a' - 'a'));
	create_cipher(cipher);
	print_cipher(cipher);

	return 0;
}

void create_cipher(int cipher[SIZE][SIZE])
{
	int r, c;

	for (c = 0; c < SIZE; c++) {
		cipher[0][c] = c - 1;
	}

	for (r = 1; r < SIZE; r++) {
		for (c = 0; c < SIZE - 1; c++) {
			cipher[r][c] = cipher[r - 1][c + 1];
		}
		cipher[r][SIZE - 1] = cipher[r][0];
	}
}
void print_cipher(int cipher[SIZE][SIZE])
{
	int r, c;

	for (r = 1; r < SIZE; r++) {
		for (c = 0; c < SIZE - 1; c++) {
			printf("%3d", cipher[r][c]);
		}
		printf("\n");
	}
}
