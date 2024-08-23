package ICC.LeetCode.medium_challengues;

import java.util.List;

/*

2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 * 
 */

public class AddTwoNumbers {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    }

    public static void main(String[] args){
        ListNode a = new ListNode();
        ListNode b = new ListNode();

        a.val = 2;
        a.next = new ListNode(4);
        a.next.next = new ListNode(3);
        printList(a);
        
        b.val = 5;
        b.next = new ListNode(6);
        b.next.next = new ListNode(4);
        printList(b);

        ListNode r = addTwoNumbers(a, b);
        printList(r);

    }
    public static void printList(ListNode l){
        String str = "";
        while( l != null){
            str += "( ";
            str += l.val;
            str += " ) -> ";
            l = l.next;
        }
        str += "( null )";
        System.out.println(str);
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2){
        ListNode result = new ListNode();
        ListNode dummy = result;
        int carry = 0;

        while( l1 != null || l2 != null || carry != 0){
            int digit1 = l1 != null? l1.val:0;
            int digit2 = l2 != null? l2.val:0;
            int sum = digit1 + digit2 + carry;
            carry = sum / 10;
            result.next = new ListNode(sum % 10);
            result = result.next;

            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
        }

        return dummy.next;

    }
}
