package ICC.Data_Structures.Stacks;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import Stack.StackX;
/**
 * Reverse a word using Stacks
 */

public class ReversingAWord {
    class StackX{
        private int maxZise = 0;
        private int top = -1;
        private char[] stackArray;

        StackX(int size){
            maxZise = size;
            top = -1;
            stackArray = new char[size];
        }

        public char pop(){
            return stackArray[top--];
        }

        public void push(char c){
            stackArray[++top] = c;
        }

        public char peek(){
            return stackArray[top];
        }

        public boolean isEmpty(){
            return ( top == -1 );
        }

    }

    public static String reverse(String word){
        StackX myStack = new StackX(word.length() - 1);
        String reversed = "";

        for(int i = 0; i < word.length(); i++){
            myStack.push(word.charAt(i));
        }

        while( !myStack.isEmpty() ){
            reversed += myStack.pop();
        }

        return reversed;
    }

    public static String geString() throws IOException{
        try{
            InputStreamReader stream = new InputStreamReader(System.in);
            BufferedReader buffer = new BufferedReader(stream);
            String s = buffer.readLine();
            return s;
        }catch(IOException ex){
            return " ";
        }
        
    }

    public static void main(String[] args){
        String input;
        String output;

        while( true ){
            input = geString();

            if (input == "exit")
                break;
            output = reverse(input);
        }
    }
    
}
