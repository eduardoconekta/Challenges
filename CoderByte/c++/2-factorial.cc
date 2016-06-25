#include <iostream>
#include <string.h> 
#include <string>
using namespace std;
void factorial()
{
	int fact;
	int res =1;
	cout<<"TECLEA UN NUMERO A FACTORIZAR \n";
	cin>>fact;
	for (int i = 1; i <= fact; ++i)
	{
		res*=i;
		cout<< ">:" <<res << endl;
	}
}

int main()
{
	factorial();
}