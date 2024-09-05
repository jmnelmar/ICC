package ICC.Data_Structures.Stacks;
/*Stack Data Structure */
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

    public static void main(String[] args){
        StackX theStack = new StackX(10);

        theStack.push(20);
        theStack.push(40);
        theStack.push(60);
        theStack.push(80);

        while(!theStack.isEmpty()){
            long value = theStack.pop();
            System.out.print(value);
            System.out.print(" ");
        }
        System.out.println("");
    }
}