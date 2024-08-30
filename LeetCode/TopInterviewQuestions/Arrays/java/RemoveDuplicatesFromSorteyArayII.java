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
        if( nums.length < 3)
            return nums.length;

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
        if( j == 0 )
            return 2;
        return j + 1;
    }

    public static int removeDuplicatesII(int[] nums){
        int cont = 1, i = 1;
        for( int j = 1; j < nums.length ; j++ ){
            if( nums[j] == nums[j - 1] )
                cont++;
            else
                cont = 1;

            if( cont <= 2 ){
                nums[i] = nums[j];
                i++;
            }
        }

        return i;
    }

    public static void main(String[] args){
        int[] nums2 = {1,1,1,2,2,3};
        String result =removeDuplicatesII(nums2) + " ";
        result += Arrays.toString(nums2);

        System.out.println(result);

        int[] nums = {0,0,1,1,1,1,2,3,3};
        result =removeDuplicatesII(nums) + " ";
        result += Arrays.toString(nums);
        System.out.println(result);

        int[] nums3 = {1,1};
        result = removeDuplicatesII(nums3) + " ";
        result += Arrays.toString(nums3);
        System.out.println(result);

        int[] nums4 = {1,1,1};
        result = removeDuplicatesII(nums4) + " ";
        result += Arrays.toString(nums4);
        System.out.println(result);

        int[] nums5 = {1,1,2};
        result = removeDuplicatesII(nums5) + " ";
        result += Arrays.toString(nums5);
        System.out.println(result);

        int[] nums6 = {1,1,2,2};
        result = removeDuplicatesII(nums6) + " ";
        result += Arrays.toString(nums6);
        System.out.println(result);

    }
    
}
