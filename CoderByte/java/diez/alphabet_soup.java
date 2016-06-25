/*
 have the function AlphajetSoup(str) 
 take the str string parameter being
  passed and return the string with the 
  letters in alphabetical order (ie. hello becomes ehllo).
   Assume numbers and punctuation symbols 
   will not be included in the string. 

	 Input = "coderbyte"Output = "bcdeeorty"
	 Input = "hooplah"Output = "ahhloop" 
*/
import java.util.Scanner;
 public class alphabet_soup{
 	public static void main(String[] args) {
 		Scanner s = new Scanner(System.in);
 		System.out.println("Enter one Word");
 		String result ="";
 		result= alphabet_soup.AlphabetSoup(s.nextLine());
 		System.out.println(result);

 		
 	}
 	public static String AlphabetSoup(String str)
 	{
 		char[] res= str.toCharArray();
 		/*
 		PUT IT ON BUBBLE METHOD 
 		char[] aux;
 		for (int i=0;i<str.length() ;i++ ) {
 			for (int j=0;j<str.length();j++ ) {
 				 if(res[j].compareTO( res[j+1] ) > 0 ) { 
                    aux[0]     = res[j]; 
                    res[j]  = res[j+1]; 
                    res[j+1]= aux[0]; 
                }    
 			}
 		}
 			*/

 		java.util.Arrays.sort (res); 
 		str = new String(res);
 		return str;
 	}
 }