/*
Using the JavaScript language, 
have the function SimpleSymbols(str) 
take the str parameter being passed and 
determine if it is an acceptable sequence
by either returning the string true or false.
 The str parameter will be composed of + and = symbols with several 
 letters between them (ie. ++d+===+c++==a) and for the string 
 to be true each letter must be surrounded by a + symbol. 
 So the string to the left would be false. The string will
  not be empty and will have at least one letter. 
*/
  import java.util.Scanner;
public class simple_simbols
{
	public static void main(String[] args) 
	{
		String res ="";
		Scanner s = new Scanner(System.in);
		System.out.println("Enter a simbol composition");
		res=simple_simbols.SimpleSymbols(s.nextLine());
		System.out.println(res);
	}
	public static String SimpleSymbols(String str)
	{
		String flag="";
		char[] parts=str.toCharArray();
		int increment=0,inc=0,i=0;
		int[] compare= new int[str.length()]; 
	
			for (i=0;i<=str.length()-1;i++ )
			{	
				if (Character.isDigit(parts[0])||Character.isLetter(parts[0])) 
				{
					flag="falso";
					break;
				}else if (Character.isDigit(parts[str.length()-1])||Character.isLetter(parts[str.length()-1]))
				{
					flag="falso";
					break;
				}

				if (Character.isDigit(parts[i])||Character.isLetter(parts[i]))
				{
					 if (Character.isLetter(parts[i+1])||Character.isDigit(parts[i+1]))
					{
						flag="falso";						
					}else if (!Character.isDigit(parts[i-1]) && !Character.isLetter(parts[i+1])) {
						flag="cierto";
					}
				}
				
			}
		return flag;
	}
			/*
			if (parts[i+1]>str.length()) {
						flag="falso";
						break;
					}else
			*/


	}

//012345678 9 10 11
//++=a==+3= +  +  c
//+d+=3=+s+

/*

			int b =0;
			System.out.println("INC: "+inc);
			while(b<inc)
			{

				System.out.println("while: "+compare[b]);
				if (compare[b]==compare[b+1]) {
					flag="cierto";
				}else if(compare[b]!=compare[b+1])
				{
					flag="falso";
					break;
				}
				b++;

			}*/
