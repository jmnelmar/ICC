/*
 * 55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array 
represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

 v
[3,2,2,0,4,3,1,2]   |   maxJump = 3; i = 0; nums[i] = 3; nums[i] + i = 3
       ^

   v
[3,2,2,0,4,3,1,2]   |   maxJump = 3; i = 1; nums[i] = 2; nums[i] + i = 3
       ^


     v
[3,2,2,0,4,3,1,2]   |   maxJump = 4; i = 2; nums[i] = 2; nums[i] + i = 4
         ^


       v
[3,2,2,0,4,3,1,2]   |   maxJump = 4; i = 3; nums[i] = 0; nums[i] + i = 3
         ^

         v
[3,2,2,0,4,3,1,2]   |   maxJump = 8; i = 4; nums[i] = 4; nums[i] + i = 8  // ends
 */

import java.util.Arrays;

public class JumpGame {
    public static boolean canJump(int[] nums) {
        int maxJump = 0, n = nums.length;
 
        for(int i = 0; i <= maxJump; i++){
            maxJump = Math.max(maxJump, nums[i] + i);
            if( maxJump >= n - 1 ) return true;
        }
        return false;
             
    }

    public static void main(String[] args){
        int[] nums = {3,2,2,0,4,3,1,2};
        System.err.println(Arrays.toString(nums));
        System.out.println(canJump(nums));

        int[] nums2 = {2,3,1,1,4};
        System.err.println(Arrays.toString(nums2));
        System.out.println(canJump(nums2));

        int[] nums3 = {3,2,1,0,4};
        System.err.println(Arrays.toString(nums3));
        System.out.println(canJump(nums3));
    }
}
