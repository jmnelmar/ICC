package ICC.linkedin.top_20_most_asked;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashSet;

public class RemoveDuplicates {
    public static void remove(int[] arr){
        HashSet<Integer> set = new HashSet<>();
        for( int n: arr ){
            set.add(n);
        }
        System.out.println(set);
    }

    public static void main(String[] args){
        int[] myArr = {1,1,2,2,3,3,3,5,5,5,5};
        remove(myArr);
    }
}
