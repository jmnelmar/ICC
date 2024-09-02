package ICC.LeetCode.Delloite;

import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;




public class TwoSum {

    public static int[] sum( int[] nums, int target ){

        int left = 0, right = nums.length - 1;
        Arrays.sort(nums);
        while( left < right ){
            System.out.println(nums[left]+","+nums[right]);
            if ( nums[left] + nums[right] > target) right--;
            else if(nums[left] + nums[right] < target) left++;
            else if(nums[left] + nums[right] == target) return new int[]{left,right};

        }

        return null;

    }

    public static int[] sumII(int[] nums, int target){
        
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for( int i = 0; i < nums.length; i++ ){
            int result = target - nums[i];
            if( map.containsKey(result) ){
                return new int[]{i, map.get(result)};
            }
            map.put(nums[i],i);
        }
        return new int[]{0};

        
    }

    public static void main(String[] args){
        int[] nums= {2,7,11,15};
        int target = 9;
        System.out.println(Arrays.toString( sumII(nums, target) ) ); 

        int[] nums2 = {3,2,4};
        target = 6;
        System.out.println(Arrays.toString( sumII(nums2, target) ) ); 
    }
    
}
