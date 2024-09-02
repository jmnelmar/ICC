package ICC.LeetCode.Delloite;
/**
 * given there is a table student( id, firstname, lastname, age, grade )
 * 1. find firstname and last name of all students with grade below 60
 * 2. firstname and last name of the youngest student with a grade above 90
 *
 
 select firstname,lastname
 where grade < 60
 join all 
 select firstname, lastname
 where grade > 90
 having min(age) = age;


 */
public class test {
    
}
