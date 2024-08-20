package ICC.ICC.LeetCode.TopInterviewQuestions.Arrays;
/*
 * Remove duplicates from a sorted array
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

 */
public class RemoveDuplicates {
    public static int removeDuplicates(int[] nums){
        if(nums.length == 0)
            return 0;
        
        int j = 0;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != nums[j]){
                j++;
                nums[j] = nums[i];
            }
        }
        return j + 1;
    }
}
