package ICC.linkedin.top_20_most_asked;

import java.util.Arrays;
import java.util.HashSet;

public class CheckAnagram {

    public static boolean IsAnagram(String str1, String str2){

        char[] aux1 = str1.toCharArray();
        char[] aux2 = str2.toCharArray();

        Arrays.sort(aux1);
        Arrays.sort(aux2);

        return Arrays.equals(aux1, aux2);
    }

    public static void main(String[] args){
        String str1 = "listen", str2="silent";
        System.out.println(IsAnagram(str1, str2));
    }
    
}
