package ICC.LeetCode.medium_challengues.utils.java;

public class LinkedList {
    
    public class Node{
        private int val;   
        private Node next;
        //public void setVal(int val){ this.val = val;}
        //public int getVal(){return this.val;}
        //public void setNext(Node next){this.next = next;}
        //public Node getNext(){return this.next;}
    
        public Node(int val, Node next){  this.val = val; this.next = next;}
        public Node(){ this.val = 0; this.next = null;};
    }


    Node head;
    public LinkedList(){this.head = null;}
    public LinkedList(Node head){this.head = head;}
    
    public void addLast(int val){
        Node node = new Node(val,null);
        if (this.head == null) this.head = node;
        else{
            Node tail = head;
            while (tail.next != null){
                tail = tail.next;
            }
            tail.next = node;
        }
       
    }

    public void addFirst(int val){
        Node node = new Node(val,null);
        Node dummy = this.head;
        if( dummy == null ) { dummy = node;}
        node.next = dummy;
        head = node;
    }

    public int length(){
        int count = 0;
        Node dummy = this.head;
        if( dummy != null){
            while( dummy != null ){
                count++;
                dummy = dummy.next;
            }
        }
        return count;
    }

    public Node getItemAt(int index){
        Node result = null;
        Node dummy = head;
        int i = 0;
        while( i != index && dummy != null ){ dummy = dummy.next; }
        result = dummy != null ? dummy : null;
        return result;
    }

    public void arrayToLinkedList(int[] array){
        for(int i = 0; i < array.length; i++){
            addLast(array[i]);    
        }
        
    }

    public int[] toArray(){
        int[] array = new int[length()];
        Node dummy = this.head;
        if( length() > 0 ){
            int i = 0;
            while( dummy != null){
                array[i] = dummy.val;
                i++;
                dummy = dummy.next;
            }
        }
        return array;
    }

    public String toString(){
        String str = "";
        Node dummy = this.head;
        while( dummy != null){
            str += "( "+ dummy.val +" ) -> ";
            dummy = dummy.next;
        }
        str += "null";
        return str;
    }

    public static void main(String[] args){
        LinkedList list = new LinkedList();
        int[] arr = {1,2,3,4,5};
        list.arrayToLinkedList(arr);
        System.out.println(list.toString());
        list.addFirst(0);
        System.out.println(list.toString());
        list.addLast(6);
        System.out.println(list.toString());

        int[] result = list.toArray();
        String str = "[";
        for( int i = 0; i < result.length; i++){
            str += i;
            str += i != result.length - 1? ", " : "";
            
        }
        str += "]";
        System.out.println(str);
    }
}
