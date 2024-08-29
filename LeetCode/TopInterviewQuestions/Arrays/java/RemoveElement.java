/*
 * https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
 * 
 * Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 */

//0 1 2 2 3 0 4 2



import java.util.Arrays;

public class RemoveElement {
    
    public static int remove(int[] nums, int val){
        int left =0, right = 0;
        int len = nums.length;

        while( left < len && right < len ){
            if( nums[right] == val ){
                right++;
            }else{
                nums[left] = nums[right];
                left++;
                right++;
            }
        }

        return left;

    }

    public static void main(String[] args){
        int[] nums = {3,2,2,3};
        int val = 3;
        int n = remove(nums, val);
        System.out.println(n);

        int[] nums2 = {0,1,2,2,3,0,4,2};
        int val2 = 2;
        n = remove(nums2, val2);
        System.out.println(n);

    }
}
