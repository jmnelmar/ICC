package ICC.ICC.JCP;

import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;
import javafx.util.Pair;

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
    
    public static Pair<Integer, Integer> countVowelsAndConsonants(String str){
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
        return Pair.of(vowels,consonants);
    }
}
