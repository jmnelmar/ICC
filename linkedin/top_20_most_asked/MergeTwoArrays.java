package ICC.linkedin.top_20_most_asked;

import java.util.Arrays;

public class MergeTwoArrays {
    
    public static int[] merge(int[] arr1, int[] arr2){
        int[] merged = new int[ arr1.length + arr2.length ];

        System.arraycopy(arr1, 0, merged, 0, arr1.length);
        System.arraycopy(arr2, 0, merged, arr1.length, arr2.length);
        return merged;
    }

    public static void main(String[] args){
        int[] arr1 = {1,2,3};
        int[] arr2 = {4,5,6};
        int[] result = merge(arr1, arr2);

        System.out.println(Arrays.toString(result));
    }
}
