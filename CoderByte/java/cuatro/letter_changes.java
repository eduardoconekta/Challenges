/*
Using the "whatelse" language, 
have the function LetterChanges(str)
 take the str parameter being passed 
 and modify it using the following 
 algorithm. Replace every letter in
  the string with the letter following 
  it in the alphabet (ie. c becomes d, z becomes a). 
  Then capitalize every vowel in this new string
   (a, e, i, o, u) and finally return this modified string.


======================================
-REMPLAZAR CADA LETRA CON LA SIGUIENTE C LE SIGUE D ETC
-LUEGO CAPITALIZAR CADA VOCAL (A,E,I,O,U) luego devolver en 
mayusculas

=======================================


*/
import java.util.Scanner;
public class letter_changes
{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String phrase="";
		System.out.println("Enter a phrase");
		phrase=in.nextLine();
		letter_changes.letterChanges(phrase);

	}
	public static int letterChanges(String a )
	{
		int size=0;
		char[] parts = a.toCharArray();
		size = parts.length;
		for (int i=0;i < size ;i++ )
		{
			char tmp;
			tmp = parts[i];
			tmp++;
			if (tmp=='a'||tmp== 'e'||tmp=='i'||tmp=='o'||tmp=='u') {
				tmp=Character.toUpperCase(tmp);
			}else if (tmp =='!') {
				tmp=' ';
			}
			parts[i]=tmp;
		}
		System.out.println(parts);
		return size;
	}
}


/*PRINT all the VOCABULARY
		char A='a';
		for (int i =0;i<26 ;++i ) {
			System.out.println("LETRA:"+A);
			A++;
		}*/