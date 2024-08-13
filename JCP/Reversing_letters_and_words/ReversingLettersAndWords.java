package ICC.ICC.JCP.Reversing_letters_and_words;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;

public class ReversingLettersAndWords {
    private static final String WHITESPACE = " ";
    public static void main(String[] args) throws IOException{
        while(1 == 1){
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Introduce a phrase type exit to stop the program");
            String parameter = reader.readLine();
            if(parameter.equals("exit"))
                break;
            System.out.println(reverseWords(parameter));

        }
       //System.out.println(reverseWords("hola mundo"));
    }

    public static String reverseWords(String str){
        String[] words = str.split(WHITESPACE);
        StringBuilder reversedString = new StringBuilder();

        for(int i = words.length - 1; i >= 0; i--){
            StringBuilder reverseWord = new StringBuilder();
            for(int j = words[i].length() - 1; j >= 0; j-- ){
                
                reverseWord.append(words[i].charAt(j));
            }
            reversedString.append(reverseWord).append(WHITESPACE);
        }
        /*
        for(String w: words){
            StringBuilder reverseWord = new StringBuilder();
            for(int i = w.length() - 1; i >= 0; i-- ){
                reverseWord.append(w.charAt(i));
            }
            reversedString.append(reverseWord).append(WHITESPACE);
        }*/

        return reversedString.toString();
    }
}
