#include <iostream>
#include <string.h> //libreria para strlen()
#include <string>
using namespace std;
void reverseword()
{	
	string word;
	int longitud=0;
	
	cout<<"Ingresa una palabra\n";
	getline(cin,word);
	longitud=word.length();
	for (int i = longitud; i >=0; i--)
	{
		cout<<word[i];
	}
	

	

}
int main ()
{
	reverseword();
}

