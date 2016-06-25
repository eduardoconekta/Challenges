import java.util.Scanner;
public class factorial
{
	public static void main(String[] args) 
	{
		int fact=0;
		Scanner i = new Scanner(System.in);
		System.out.println("Ingresa un numero");	
		fact=i.nextInt();
		int funcion= new factorial(fact);
		System.out.print(","+funcion);
	}
	public int factorial(int v)
	{

		return v+factorial(v-1); 

	}
}
