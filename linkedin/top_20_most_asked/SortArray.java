package ICC.linkedin.top_20_most_asked;

import java.lang.reflect.Array;
import java.util.Arrays;

public class SortArray {

    public static void sort(int[] arr){
        Arrays.sort(arr);
    }

    public static void printArray(int[] arr){
        String str = "[ ";
        for( int i = 0; i < arr.length; i++){
            str += arr[i];
            if (i != arr.length -1){
                str += ", ";
            }
        }
        str+=" ]";
        System.out.println(str);
    }

    public static void main(String[] args){
        int[] nums = {3,5,1,4,2};
        printArray(nums);
        sort(nums);
        printArray(nums);
    }
    
}
