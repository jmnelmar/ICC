package ICC.linkedin.top_20_most_asked;

public class ReverseString {

    public static String reverse(String str){
        StringBuilder reversed = new StringBuilder(str).reverse();

        return reversed.toString();
    }

    public static void main(String[] args){
        String str = "Autonomous";
        System.out.println(str);
        System.out.println(reverse(str));
    }

}
