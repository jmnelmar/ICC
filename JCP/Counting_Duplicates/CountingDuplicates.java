package ICC.ICC.JCP.Counting_Duplicates;

import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class CountingDuplicates{
  
    public static void main(String[] args) throws IOException{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Introduce a word");
        String parameter = reader.readLine();
        System.out.println( countingDuplicates(parameter) );

        
    }
    
    //Using Hashmap and compute method
    public static Map<Character, Integer> countingDuplicates(String word){

        Map<Character, Integer> result = new HashMap<>();
        for(int i = 0; i < word.length(); i++){
            char ch = word.charAt(i);
            result.compute(ch, (k,v) -> ( v == null )? 1 : ++v );
        }

        return result;
    }

    //Using stream 
}