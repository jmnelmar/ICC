package ICC.ICC.JCP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class CheckingDigits {
    public static void main(String[] args) throws IOException{

        while( 1 == 1){
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Introduce a phrase - type exit to close the program");
            String input = reader.readLine();
            if(input.equals("exit"))
                break;
            System.out.println(CheckDigits(input));
        }      
    }

    public static boolean CheckDigits(String str){

        for(int i = 0; i< str.length(); i++){
            if( !Character.isDigit(str.charAt(i)) )
                return false;
        }

        return true;

    }
    /*
     * contains only digict with Java 8 stream methods
    */
    public static boolean containsOnlyDigit(String str){
        return !str.chars().anyMatch(n->!Character.isDigit(n));
    }

    /**
     * Solution usign string matches 
     * this method returns a boolean value indicating whether or not this string matches the given regular expresion
     */
    public static boolean containsOnlyDigitII(String str){
        return str.matches("[0-9]+");
    }
}
