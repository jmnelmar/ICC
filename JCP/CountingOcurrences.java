
public class CountingOcurrences {
    public static void main(String[] args){
        String str =  "anona";
        System.out.println(countOcurrencesOfACharacter(str,"a"));
    }
    
    public static int countOcurrencesOfACharacter(String str, String ch){
        if(ch.codePointCount(0, ch.length()) > 1)
            return -1;
        int result =  str.length() - str.replace(ch, "").length();
        return ch.length() == 2?result/2:result;
    }
}
