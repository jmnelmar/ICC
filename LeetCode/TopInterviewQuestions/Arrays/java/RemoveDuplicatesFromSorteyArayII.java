import java.lang.reflect.Array;
import java.util.Arrays;

/**
 * [0,0,1,1,1,1,2,3,3]
 *  
  
    
                    v
 * [0,0,1,1,2,3,3,3,3]
                ^ 
   
 */

public class RemoveDuplicatesFromSorteyArayII {

    public static int removeDuplicates(int[] nums){

        int j = 0;

        for(int i = 0; i < nums.length; i++){
            if( nums[j] != nums[i] ){
                if(nums[j] == nums[j + 1] )
                    j += 2;
                else
                    j++;

                nums[j] = nums[i];
            }else if( nums[j] == nums[i] && nums[j + 1] != nums[j] ){
                j++;
                nums[j] = nums[i];
            }

        }
        return j + 1;
    }

    public static void main(String[] args){
        int[] nums2 = {1,1,1,2,2,3};
        String result =removeDuplicates(nums2) + " ";
        result += Arrays.toString(nums2);

        System.out.println(result);

        int[] nums = {0,0,1,1,1,1,2,3,3};
        result =removeDuplicates(nums) + " ";
        result += Arrays.toString(nums);
        System.out.println(result);
    }
    
}
