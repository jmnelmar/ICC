
package ICC.ICC.JCP.FIrstUniqueChar;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
public class FirstUniqueChar {

    public static void main(String[] args) throws IOException{
        while(1 == 1){
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Introduce a word - type exit to stop the program");
            String parameter = reader.readLine();
            if(parameter.equals("exit") )
                break;
            System.out.println( firstNonRepeatedCharacterII(parameter) );
        
        }
        
    }

    public static Character firstNonRepeatedCharacter(String word){
        Map<Character,Long> result = new HashMap<>();
        Character ch = ' ';
        for(int i = 0; i < word.length(); i++){
            char c = word.charAt(i);
            result.compute(c, (k,v) -> v == null?1: ++v );
        }
        System.err.println(result);
        for(Character key: result.keySet()){
            if(result.get(key) == 1){
                ch = key;
                break;
            }
        }

        return ch;

    }

    /*
     * Using LinkedHashMap
     */
    public static char firstNonRepeatedCharacterII(String word){
        Map<Character, Integer> chars = new LinkedHashMap<>();

        for(int i = 0; i < word.length(); i++){
            char ch = word.charAt(i);
            chars.compute(ch, (k,v) -> v == null?1:++v );
        }

        for(Map.Entry<Character,Integer> entry: chars.entrySet()){
            if(entry.getValue() == 1){
                return entry.getKey();
            }
        }

       return Character.MIN_VALUE;

    }
    
}
