#include <stdio.h>
#include <stdlib.h>
#include <string.h>
longestWord()
{ 
	char coment[80];
	char save[80];
	char *bigword;
	int bigger =0;
	int cont=0;
	int lon =0;
	int lon2 =0;
	int i;
	printf("INGRESA UN COMENTARIO\n");
	gets(coment);
	//SCANF solo captura caracteres, no espacios
	lon = strlen(coment);
	for (i = 0; i < lon; ++i)
	{
		if (coment[i]== ' ')
		{
			printf("Hay un espacio\n");
			cont =0;
			strcpy(save,"");
		}else
		{	
			strcpy(save,coment);
			cont++;
			if (cont>=bigger)
			{
				bigger = cont;
			}
			

		}
	}
	printf("No de letras %i, Palabra: %s \n",bigger, save);
}

int main(int argc, char const *argv[])
{
	longestWord();
	return 0;
}

//IS  IN THERE A LITTLE BUG THAT DONT LET TO STORE THE FINISH LONGEST WORD AND SHOW THAT