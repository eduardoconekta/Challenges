/*
have the function TimeConvert(num)
 take the num parameter being passed and 
 return the number of hours and minutes the 
 parameter converts to (ie. if num = 63 then 
 the output should be 1:3). Separate the number 
 of hours and minutes with a colon. 

 Input = 126 Output = "2:6"
Input = 45 Output = "0:45" 
*/
import java.util.Scanner;
public class time_convert {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String date = "";
		System.out.println("Enter a Number");
		date = time_convert.TimeConvert(s.nextInt());
		System.out.println(date);

	}

	public static  String TimeConvert(int num)
	{
		String res="";
		if (num >60) {
		//HOURS
			res = (num/ 60 )+":";
		//MINUTES
			res += (num %60);

		}else if (num<60) {
			res="0:"+num;
		}

		return res;
	}
}