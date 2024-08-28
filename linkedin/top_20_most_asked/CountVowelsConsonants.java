package ICC.linkedin.top_20_most_asked;

import java.util.HashMap;
import java.util.Map;

public class CountVowelsConsonants {
    
    public static int CountVowels(String str){
        int vowles = 0;
        int consonants = 0;
        for(char c:str.toCharArray()){
            if("aeiouAEIOU".indexOf(c) != -1){
                vowles++;
            }
        }



        return vowles;
    }

    public int CountConsonants(String str){
        int consonants = 0;

        for(char c: str.toCharArray()){
            if( "aeiouAEIOU".indexOf(c) == -1){
                consonants++;
            } 
        }

        return consonants;
    }



    public static void main(String[] args){
        String str = "anona";
        System.out.println(CountVowels(str));
    }
} 
