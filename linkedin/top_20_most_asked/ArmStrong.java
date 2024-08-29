package ICC.linkedin.top_20_most_asked;

public class ArmStrong {

    /* method to get the digits in a number */
    public static int digits(int n){
        int temp = n;
        int result = 0;
        while(temp != 0){
            result++;
            temp /= 10;
        }
        return result;
    }
    /*
     * Armstromg numbers are that numbers whic the sumatory of its digits each raised to the len of its digits
     * example 153 = (1^3)+(5^3)+(3^3)
     */
    public static boolean IsAsStromg(int n){

        int temp = n;
        int len = digits(n);/*Calculating the lenght of the digits*/
        int sum = 0;
        while(temp != 0){
            int digit = temp %  10; /* geting the current digit */
            sum += Math.pow(digit, len);
            temp /= 10; /* removing the last digit(moving to the next left digit) */
        }
        
        if( sum == n)
            return true;

        return false;

    }

    public static void main(String[] args){
        int n = 153;
        System.out.println(IsAsStromg(n));
    }


    
}
