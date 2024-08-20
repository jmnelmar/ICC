/*
 * Consider you have been given an array m and an integer k write a code to rotate the array m, k times
 *  
 */

import java.util.Arrays;

public class RotatingAnArrayKtimes {
    public static void main(String[] args) {

        int A[] = {5, 5, 2, 3, 1, -2, 33, -1};
        int k = 5;
        
        System.out.println("Before: " + java.util.Arrays.toString(A));
        
        rotate(A, k);
        
        System.out.println("After: " + java.util.Arrays.toString(A));
    }

    public static void rotate(int[] m, int k){
        int[] cm = m.clone();
        int len = m.length;

        for(int i = 0; i < len; i++){
            m[ (i + k) % len ] = cm[i];
        }
    }


}


/**
 * [1,2,3,4,5,6,7] k = 3 len = 7
 * 
 * i = 0   ( i + k ) % len = 3  m[3]
 * 
 */