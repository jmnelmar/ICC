package ICC.linkedin.top_20_most_asked;

public class CountDIgitsInNumbers {

    public static int digits(int number){
        return  String.valueOf(number).length();
    }

    public static int digitsII(int number){
        int temp = number;
        int result = 0;

        while(temp != 0){
            result++;
            temp /= 10;
        }
        return result;
    }

    public static void main(String[] args){
        int number = 12345;
        System.out.println(digits(number));
        System.out.println(digitsII(number));
    }
    
}
