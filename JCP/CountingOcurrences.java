
public class CountingOcurrences {
    public static void main(String[] args){
        String str =  "anona";
        System.out.println(countOcurrencesOfACharacter(str,"a"));
    }
    
    public static int countOcurrencesOfACharacter(String str, String ch){
        return str.length() - str.replace(ch, "").length();
    }
}
