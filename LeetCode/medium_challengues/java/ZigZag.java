/*
 * 6. Zigzag Conversion
Medium
Topics
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)


And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
P   A   H   N
A P L S I I G
Y   I   R

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

PI
AL
YA
P

Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
 */
package ICC.LeetCode.medium_challengues.java;

public class ZigZag {
    
    public static String convert(String s, int rownum){
        if(rownum == 1)
            return s;
        
        int direction = 0, row = 0;
        StringBuilder[] builder = new StringBuilder[rownum];
        for(int i = 0; i < rownum; i++){
            builder[i] = new StringBuilder();
        }

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            
            row += direction;
            builder[row].append(c);
            
            //System.out.println("character: "+c+" row: "+row);

            if( row == 0 || row == rownum - 1 )
                direction = ( direction == 0 ) ? 1: -direction;
        }

        StringBuilder result = new StringBuilder();
        for( StringBuilder sb: builder){
            result.append(sb);
        }
        return result.toString();

    }

    public static void main(String[] args){
        System.out.println(convert("PAYPALISHIRING", 4));
    }
}
