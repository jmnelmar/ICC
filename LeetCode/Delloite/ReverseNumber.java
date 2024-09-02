package ICC.LeetCode.Delloite;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class ReverseNumber {

    public static int reverse(int x) {

        int sign = 1;
        if (x < 0){
            sign = -1;
            x *= sign;
        }
        try{
            String chars = String.valueOf(x);
            StringBuilder builder = new StringBuilder(chars);
            builder.reverse();

            return Integer.parseInt(builder.toString()) * sign;
        }catch(Exception ex){
            return 0;
        }
        
    }

    public static void main(String[] args){
        int number = 1534236469;
        int reversed = reverse(number);
        System.out.println(reversed);

    }

    
}


