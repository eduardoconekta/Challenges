#include <stdio.h>
#include <stdlib.h>
#include <string.h>


	char reverseword()
	{	
		int longitud=0;
		int i=0;
		char word[20];
		printf("ingrese una palabra \n");
		scanf("%s",word);
		longitud=strlen(word);
		i=longitud;
		while (i>0)
			{		
				i--;
				printf("%c\n",word[i]);	
			}
		return;
	}
void main()
{
	reverseword();

}