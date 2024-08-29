package ICC.linkedin.top_20_most_asked;

import java.util.Arrays;

public class FindTheLargestElement {

    public static int findTheLargest(int[] arr){
        Arrays.sort(arr);
        return arr[arr.length - 1];
    }

    public static void main(String[] args){
        int[] arr = {1,3,5,100,7,9};
        System.out.println(findTheLargest(arr));
    }
    
}
