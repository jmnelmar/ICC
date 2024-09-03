package ICC.Data_Structures.Stacks;

public class StackX {
    private int maxSize;
    private long[] stackArray;
    private int top;


    public StackX(int s){
        stackArray = new long[s];
        maxSize = s;
        top = -1;
    }

    public void push(long item){
        stackArray[++top] = item;
    }

    public long peek(){
        return stackArray[top];
    }

    public long pop(){
        return stackArray[top--];
    }

    public boolean isEmpty(){
        return (top == -1);
    }

    public boolean isFull(){
        return ( top == maxSize - 1);
    }

    
}
