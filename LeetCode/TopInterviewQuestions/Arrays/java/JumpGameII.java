/*
 * 45. Jump Game II
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], 
you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
 */

import java.util.Arrays;

public class JumpGameII {

    public static int jump(int[] nums) {
         // The starting range of the first jump is [0, 0]
       int maxJump = 0, jumps = 0, n = nums.length, jumpEnd = 0;

       for(int i = 0; i < n - 1; i++){
            // Update the farthest reachable index of this jump.
            maxJump = Math.max(maxJump, nums[i] + i);

            // If we finish the starting range of this jump,
            // Move on to the starting range of the next jump.
            if( i == jumpEnd ){
                jumps++;
                jumpEnd = maxJump;
            }
       }
       return jumps;
    }

    public static void main(String[] args){
        int[] nums = {2,3,1,1,4};
        String str = Arrays.toString(nums) + " ";
        str += jump(nums) + " jumps";
        System.out.println(str);
        
        int[] nums2 = {2,3,0,1,4};
        str = Arrays.toString(nums2) + " ";
        str += jump(nums2) + " jumps";
        System.out.println(str);

        int[] nums3 = {3,2,2,0,4,3,1,2};
        str = Arrays.toString(nums3) + " ";
        str += jump(nums3) + " jumps";
        System.out.println(str);

    }
    
}
