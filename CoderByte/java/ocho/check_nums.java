/*
have the function CheckNums(num1,num2) 
take both parameters being passed and 
return the string true if num2 is greater than num1, 
otherwise return the string false. 
If the parameter values are equal to each other then return the string -1. 

 Input = 3 & num2 = 122Output = "true"
Input = 67 & num2 = 67Output = "-1" 
*/
import java.util.Scanner;
public class check_nums
{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String res="";
		int a=0,b=0;
		System.out.println("Enter two numbers");
		a=s.nextInt();
		b=s.nextInt();
		res=check_nums.CheckNums(a,b);
		System.out.println(res);
	}
	public  static String CheckNums(int num1,int num2)
	{
		String result="";
		if (num2>num1) {
			result="true";
		}else if (num2<num1) {
			result="false";
		}else if (num2==num1) {
			result="-1";	
		}
		return result;
	}

}