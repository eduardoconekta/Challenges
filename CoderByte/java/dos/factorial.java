import java.util.Scanner;
public class factorial
{

	public static void main(String[] args) 
	{
		/*
			Inicializamos val en 0 para que despues 
			la utilicemos mediante la variable con 
			la que hacemos referencia a Scanner que 
			es i 

				Syste.out.print("ingresa un numero >:")
				i.nextInt [Esto lee el numero siguiente que se ingrese]

				////////////////VISTA AL USUARIO///////////////

				INGRESA UN NUMERO >:

			despues se manda a traer la clase primero 
			instanciamos factorial con la var n y 
			despues con la var n podemos acceder al
			cuerpo de la clase que contiene la funcion 
			factor
		*/
		int val=0;
		factorial n = new factorial();
		Scanner i = new Scanner(System.in);
		System.out.print("Ingresa un numero \n\t>:");	
		val=i.nextInt();
		System.out.print("Resultado  "+n.factor(val));
	}

	/*
	Funcion que realiza el numero de repeticiones dependiendo
	el valor que se le de a la variable "a" de la funcion de 
	abajo en este caso es int a y esta toma el valor de la var
	"val" de arriva


	val = 5
	res = 1
	a = val
		for(d=1;d<=a;d++)
		{
			1*=1;
			1*=2;
			3*=3;
			6*=4;
			24*=5;
			res=120;
		}
		return [SERIE DE ITERACION] + RESULTADO;
	*/
	public int factor(int a)
	{
		int res=1;
		for (int d=1;d<=a;d++)
		{
			res*=d;
			System.out.println("\n>>:"+res);
			
		}
		return res;
	}

}
