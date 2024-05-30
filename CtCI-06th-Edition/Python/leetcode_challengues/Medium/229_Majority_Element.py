'''
229. Majority Element II
Medium
Topics
Companies
Hint
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?
'''
from collections import Counter
import pytest

def majorityElement(nums:[int]) -> [int]:
    majority_elements= []
    count = 0
    treshold = len(nums) // 3
    elements = Counter(nums)

    for element, count in elements.items():
        if count > treshold:
            majority_elements.append(element)
    
    return majority_elements

@pytest.mark.parametrize(
    'nums,output,expected',
    [
        ([3,2,3],[3],True),
        ([1],[1],True),
        ([1,2],[1,2],True),
        ([1, 2, 2, 4, 4, 4],[4],True),
        ([1, 2, 2, 2, 4, 4, 4],[2,4],True),
        ([1, 1, 2, 2, 2, 4, 4, 4],[2,4],True),
        ([1, 1, 1, 2, 2, 2, 4, 4, 4],[],True)
     ]
)
def test_majorityElement(nums, output, expected):
    assert (majorityElement(nums) == output) == expected