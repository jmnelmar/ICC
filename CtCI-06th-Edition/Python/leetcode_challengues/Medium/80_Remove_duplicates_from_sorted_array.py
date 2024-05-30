'''
80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most 
twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part 
of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold 
the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
'''

def removeDuplicates( nums:[int]) -> int:
    count = 0
    while count < len(nums):
        if nums.count(nums[count]) > 2:
            del nums[count]
        count += 1

    print(nums)
    return len(nums)

def removeDuplicatesIIPointers(nums:[int]):
    #Edge scenario if lenght of nums is less than or equal to 2, return length 
    if len(nums) <= 2:
        return len(nums)
    #Initialize slow pointer
    slow = 2

    #Iterate throught the array with the fast pointer
    for fast in range(2,len(nums)):
        # If current element is not equal to element at slow - 2
        if nums[fast] != nums[slow - 2]:
            #update element at Slow and increment slow
            nums[slow] = nums[fast]
            slow += 1
    
    #Return the lenght of the modified array 
    return slow

#           f
# 1,1,2,2,3,3
#           s
#nums = [1,1,1,2,2,3]
#removeDuplicates(nums)

#nums = [0,0,1,1,1,1,2,3,3]
#removeDuplicates(nums)
from collections import Counter
nums = [3,2,3]

dic = Counter(nums)
maxx = 0
result = 0
for key in dic.keys():
    if dic[key] > maxx:
        result = key
        maxx = dic[key]
    
print(result) 