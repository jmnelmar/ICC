'''
713. Subarray Product Less Than K
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
'''
import pytest
#this solution works but exceed the time limit
def numSubarrayProductLessThanK( nums: [int], k: int) -> int:
    left,right = 0,0
    subarrays = []
    arr  = []
    while left < len(nums):
        arr = nums[left:right+1]
        product = 1
        for i in range(len(arr)):
            product *= arr[i] 
        if product < k:
            subarrays.append(arr) 
        right += 1
        if right > len(nums) - 1:
            left += 1
            right = left
            product = 1

    return len(subarrays)
    
#second approach instead to iterate again to calculate the product, consider to only calculate the product with the left and right pointer
def numSubarrayProductLessThanK2ndAproach( nums: [int], k: int) -> int:
    if k < 1:
        return 0
    
    count, left, product = 0, 0, 1
    for right, num in enumerate(nums):
        product *= num
        while product >= k:
            product //= nums[left]
            left +=1
        count += right - left + 1

    return count

@pytest.mark.parametrize(
    'nums,k,output,expected',
    [
        ([10,5,2,6],100,8,True)
    ]
)
def test_product(nums,k,output,expected):
    assert (numSubarrayProductLessThanK2ndAproach(nums,k) == output) == expected

#nums=[10,5,2,6]
#Sum = sum(nums)
#print(Sum)
#print(numSubarrayProductLessThanK2ndAproach(nums,100))