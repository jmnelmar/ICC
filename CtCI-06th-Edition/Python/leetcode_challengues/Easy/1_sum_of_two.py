'''
1. Two Sum
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''
import pytest

def twoSum( nums: [int], target: int) -> [int]:
    left, right = 0, len(nums) - 1
    while left < right: 
        summ = nums[left] + nums[right]
        if summ == target:
            return [left,right]
        elif summ > target:
            right -=1
        elif summ < target:
            left += 1
    return []

def twosumII(nums, target):
    left,right = 0, 0

    while left < len(nums) - 1:
        if nums[left] + nums[right +1] == target:
            return [left, right + 1]
        else:
            right += 1
            if right >= len(nums) - 1:
                left += 1
                right = left
    

@pytest.mark.parametrize(
    'nums,target,output,expected',
    [
        ([2,7,11,15],9,[0,1],True),
        ([3,3],6,[0,1],True),
        ([3,2,4],6,[1,2],True)
    ]
)
def test_twoSum(nums, target, output,expected):
    assert twosumII(nums,target) == output
   
