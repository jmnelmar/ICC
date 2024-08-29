package ICC.linkedin.top_20_most_asked;

import java.util.Arrays;

public class FIndMissingNumber {

    public static int missing(int[] arr){
        Arrays.sort(arr);
        int n = arr.length + 1;
        int s =  (n *( n + 1)) / 2;

        for( int a: arr ){
            s -= a;
        }

        return s;
    }

    public static void main(String[] args){
        int[] numbers = {1,2,4,5,6};
        System.out.println(missing(numbers)); 
    }
    
}
