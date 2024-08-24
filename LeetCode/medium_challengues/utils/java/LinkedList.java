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
    
    public void addLast(Node node){
        Node dummy = this.head;
        if(dummy == null){ dummy = node; }
        while(dummy.next != null){
            dummy = dummy.next;
        }
        dummy.next = node;
    }

    public void addFirst(Node node){
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

}
