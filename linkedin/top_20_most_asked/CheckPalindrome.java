package ICC.linkedin.top_20_most_asked;

public class CheckPalindrome {
    
    public static boolean IsPalindrome(String str){
        StringBuilder strb = new StringBuilder(str).reverse(); 
        if(!strb.toString().equals(str))
            return false;

        return true;
    }

    public static boolean IsPalindromeII(String str){
        int left = 0;
        int right = str.length() - 1;
        
        while( left < right ){
            if(str.charAt(left) !=  str.charAt(right)){
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }

    public static void main(String[] args){
        String str = "ana";
        System.out.println(str);
        System.out.println(IsPalindrome(str));
        System.out.println(IsPalindromeII(str));
    }
}
