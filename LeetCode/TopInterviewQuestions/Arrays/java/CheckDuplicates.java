import java.util.HashMap;
import java.util.Map;
public class CheckDuplicates {

    public static void main(String[] args){
        int[] nums = {1,2,3,4,5,5,6,7};
        System.out.println(CountingDuplicates(nums));
        int[] numsII = {1,2,3,4,5,6,7};
        System.out.println(CountingDuplicates(numsII));
    }

    public static boolean CountingDuplicates(int[] nums){
        Map<Integer, Integer> map_nums = new HashMap<Integer, Integer>();
        for(int n: nums){
            if(map_nums.containsKey(n))
                return true;
            else    
                map_nums.put(n, 1);
        }
        return false;
    }
    
}
