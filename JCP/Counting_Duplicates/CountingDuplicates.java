package ICC.ICC.JCP.Counting_Duplicates;

import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class CountingDuplicates{
  
    public static void main(String[] args) throws IOException{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Introduce a word");
        String parameter = reader.readLine();
        System.out.println( countDuplicates(parameter) );
        System.out.println( countDuplicatesII(parameter) );

        
    }
    
    //Using Hashmap and compute method
    /*
     * This solution has three steps. The first two steps are meant to transform the given string 
     * into Stream<Character>, while the last steps is responsible for grouping and counting the characters.
     */
    public static Map<Character, Integer> countDuplicates(String word){
        /*
         * Steps.
         * 1. Call the String.chars() methond on the original string. This will return IntStream. IntStream 
         *    contains an integer representation of the characters for the given string
         * 2. Trnasform IntStream into stream of characters via the mapToObj() method (convert the integer 
         *    representation into human-frinedly character form).
         * 3. Finally group characters  (Collectors.groupBy()) and count them (Collectors.counting()).
         */
        Map<Character, Integer> result = new HashMap<>();
        for(int i = 0; i < word.length(); i++){
            char ch = word.charAt(i);
            result.compute(ch, (k,v) -> ( v == null )? 1 : ++v );
        }

        return result;
    }

    //Using stream 
    public static Map<Character, Long> countDuplicatesII(String word){
        Map<Character,Long> result =  word.chars().
                                        mapToObj(c -> (char)c).
                                        collect(Collectors.groupingBy(c->c,Collectors.counting()));
        return result;
    }

    /*  Counting duplicates includin unicode characters
    *   to include unicode characters are composed for two values a hig value and a low values this is known 
    *   as surrogate pair, when we are dealing with unicode we only need one of the pair and skip the other
    *   value in teh pair.
    *   to identify if the character is an unicode is using the codePintAt function to get the numeric value
    *   of the character, next get the value of the chars and finally using charCount if this return 2 values
    *   we have a unicode in this char with the pair in the string, get the first one and skip the second one
    *   by increasing the counter.
    */

    public static Map<String, Integer> countDuplicatesIII(String word){
        Map<String,Integer> result = new HashMap<>();

        for(int i = 0; i < word.length(); i++){
            int cp = word.codePointAt(i);
            String ch = String.valueOf(Character.toChars(cp));
            if(Character.charCount(cp) == 2){// 2 means surrogate pair
                i++;//skping the next value.
            }
            result.compute(ch, (k,v) -> (v == null)?1:++v);
        }

        return result;
    }
}