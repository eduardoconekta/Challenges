#include <stdio.h>
#include <stdlib.h>
#include <string.h>

	int factorial()
	{
		int factor;
		int res = 1;
		int i;
		printf("INGRESA UN NUMERO A FACTORIZAR\n >:");
		scanf("%i",&factor);
		for ( i = 1; i <= factor; ++i)
		{
			res*=i;
			printf(">: %i \n",res);
		}
	return 0;

	}

int main(int argc, char const *argv[])
{
	factorial();

}