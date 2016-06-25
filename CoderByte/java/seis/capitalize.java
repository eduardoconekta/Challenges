/*
 Using the whatelse language,
  have the function LetterCapitalize(str) 
  take the str parameter being passed and 
  capitalize the first letter of each word.
   Words will be separated by only one space. 
*/
import java.util.Scanner;
public class capitalize{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String res="";
		System.out.println("Ingresa una frase");
		res  = capitalize.LetterCapitalize(s.nextLine());
		System.out.println(res);
	}

	public static String LetterCapitalize(String str)
	{
		char[] w_part=str.toCharArray();
		for (int i=0;i<str.length() ;i++)
		{
			if(w_part[i]==w_part[0])
			{
				w_part[0]=Character.toUpperCase(w_part[0]);
			}
			else if(w_part[i-1]==' ')
			{

				w_part[i]=Character.toUpperCase(w_part[i]);

			}			
		}
		String result = new String(w_part);
		return result;

	}
}