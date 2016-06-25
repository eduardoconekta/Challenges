import java.util.Scanner;
public class longestring
{
	public static void main(String[] args) {
		Scanner leer = new Scanner(System.in);
		String frase = "";
		System.out.println("Ingresa una frase");
		longestring.longestWord(leer.nextLine());
	}
	public static void longestWord(String line)
	{
		int longitud=0,bigger=0;
		String word="",save="";
		for (int i =0; i < line.length();i++) {
			if (line.charAt(i)==' ')
			{
				longitud=0;
				word="";
			}
			else 
			{
				longitud++;
				word+=line.charAt(i);
				bigger=(longitud>bigger)?longitud:bigger;
				save=(word.length()>=bigger)?word:save;	
			}

		}
		System.out.println("Palabra mas larga fue de "+bigger+" Letras, \n>:"+save);
	}
}
//PENDIENTE PRIMERO EN ENTRAR CON LA MAYOR LONGITUD PRIMERO EN SALIR 