package ICC.linkedin.top_20_most_asked;

public class ReversingNumbers { 

    public static int reverse(int n){
        String result = "";
        int temp = n;

        while(temp != 0){
            int digit = temp % 10;
            result += digit;
            temp /= 10;
        }

        return Integer.parseInt(result);
    }

    public static void main(String[] args){
        int n = 153;
        System.out.println(reverse(n));
    }
    
}
