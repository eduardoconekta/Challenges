/*
 Using the JavaScript language,
  have the function SimpleAdding(num)
   add up all the numbers from 1 to num.
    For the test cases, the parameter num will
     be any number from 1 to 1000. 
*/
 import java.util.Scanner;
public class simple_adding{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int res=0;

		System.out.println("Enter a number betwen 1 and 1000"); 
		res=simple_adding.SimpleAdding(s.nextInt());
		System.out.println("Result "+res);

	}
	public static int SimpleAdding(int num)
	{
		int i,concat=0;
		for (i=1;i<=num ;++i )concat+=i;
		return concat;
	}
}