package ICC.ICC.JCP;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

public class CountingVowelsAndConsonants {
    /* 
     * A first aproach for this problem requires traversing the 
     * string characters and doing the following
     * 
     * 1. We need to check whether the current character is 
     *    a vowel(this is convenient since we only have five
     *    pure vowels in English)
     * 2. If the current character is not a vowel, then check
     *    whether it sits between 'a' and 'z'(this means that
     *    the current character is a consonant)
    */

    private static final Set<Character> allVowels = new HashSet(Arrays.asList('a','e','i','o','u'));
    
    public static List<Integer> countVowelsAndConsonants(String str){
        str = str.toLowerCase();
        int vowels = 0;
        int consonants = 0;
        
        for(int i = 0; i < str.length(); i++){
            char ch = str.charAt(i);
            if(allVowels.contains(ch))
                vowels++;
            else if(ch >= 'a' && ch <= 'z')
                consonants++;
        }
        List<Integer> result = new ArrayList<>();
        result.add(vowels);
        result.add(consonants);
        return result;
    }

    /*
     * Solution using Java 8 style
     */
    public static List<Integer> countVowelsAndConsonantsII(String str){
        
    }

    public static void main(String[] args) throws Exception{
        while(1==1){
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Introduce a phrase - type exit to close the program");
            String input = reader.readLine();
            if(input.equals("exit"))
                break;
            List<Integer> result = countVowelsAndConsonants(input);

            System.out.println("vowels: "+result.get(0)+", consonants: "+result.get(1));
        }
    }
}
