package ICC.LeetCode.medium_challengues.utils.java;
import ICC.LeetCode.medium_challengues.utils.java.LinkedList;
public class LinkedListTest {

    public static void main(String[] args){
        LinkedList list = new LinkedList();
        int[] arr = {1,2,3,4,5};
        list.arrayToLinkedList(arr);
        System.out.println(list.toString());
    }
    
}
