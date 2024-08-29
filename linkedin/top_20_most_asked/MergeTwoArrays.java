package ICC.linkedin.top_20_most_asked;

import java.util.Arrays;

public class MergeTwoArrays {
    
    public static int[] merge(int[] arr1, int[] arr2){
        int[] merged = new int[ arr1.length + arr2.length ];

        System.arraycopy(arr1, 0, merged, 0, arr1.length);
        System.arraycopy(arr2, 0, merged, arr1.length, arr2.length);
        return merged;
    }

    public static void mergeII(int[] nums1, int m, int[] nums2, int n){
        System.arraycopy(nums1, 0, nums1,0, m);
        System.arraycopy(nums2, 0, nums1, m, n);
        Arrays.sort(nums1);

    }

    public static void main(String[] args){
        int[] arr1 = {1,2,3};
        int[] arr2 = {4,5,6};
        int[] result = merge(arr1, arr2);
        System.out.println(Arrays.toString(result));

        int[] arr3 = {1,2,3,0,0,0};
        int[] arr4 = {4,5,6};
        int m = 3, n = 3;

        mergeII(arr3, m, arr4, n);
        System.out.println(Arrays.toString(arr3));
        
    }
}
