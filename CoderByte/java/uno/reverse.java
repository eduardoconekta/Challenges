import java.util.Scanner;
public class reverse
{


	public static void main(String[] args)
	{	
		String chain="";
		Scanner data=new Scanner(System.in);
		System.out.println("Ingresa tu texto");
		chain=data.nextLine();
		System.out.println(reverse.reverseword(chain));
	}

	public static String reverseword(String a)
	{
		char b[]=a.toCharArray();
		String word="";
		for (int i=a.length() -1;i>=0 ;i--) 
		{
			word+=b[i];			
		}

		return word;
	}
}