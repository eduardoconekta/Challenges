#include <iostream>
#include <string.h> //libreria para strlen()
#include <string>
using namespace std;
void longestWord()
{
	string coment;
	int com_len;
	int counter=0;
	cout<<"INGRESA UNA FRASE LARGA\n";
	cin>>coment;
	cout<<coment;
	com_len=coment.length();
	const char * space=coment.c_str();
	for (int i = 0; i < com_len; ++i)
	{
		cout<<space[i];
		if (space[i] == ' ')
		{
			cout<<"White Space";
			counter=0;
		}else
		{
			counter++;
		}
	}
	/* CONVERT STRING TO CHAR
	string l="Pranav";
	char *p;
	p=(char *) l;
	*/
	
}



int main(int argc, char const *argv[])
{
	longestWord();
	return 0;
}