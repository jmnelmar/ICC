package ICC.LeetCode.medium_challengues.java;
/*
 * Leet code problem
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 */
import java.util.Map;
import java.util.HashMap;
public class LongestSubString {
    public static int lengthOfLongestSubstring(String s) {
        int result = 0;
        int left = 0;
        int right = left + 1;
        Map<String,Integer> chars = new HashMap<>();
        
        while( left < right && right < s.length() ){
            String str = s.substring(left, right);
            result = str.length() > result? str.length():result;
            right += 1;
        } 
        return result;

    }

    public static void main(String[] args){
        
    }
}
