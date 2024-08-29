package ICC.linkedin.top_20_most_asked;

import java.util.Arrays;

public class SecondLargestInAnArray {

    public static int findSecondLargest(int[] arr){
        if(arr.length == 0)
            return 0;
        else if(arr.length == 1)
            return arr[0];
        Arrays.sort(arr);
        return arr[arr.length - 2];
    }

    public static void main(String[] args){
        int[] arr = {12, 35, 1, 10, 34, 1};
        System.out.println(findSecondLargest(arr));
    }
    
}
