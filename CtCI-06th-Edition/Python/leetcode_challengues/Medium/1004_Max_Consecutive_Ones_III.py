'''
1004. Max Consecutive Ones III

Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 
1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''
import pytest
def longestOnes( nums:[int], k: int) -> int:
    maxx, zeros, l = 0,0,0

    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1

        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1

        maxx = max(maxx, (r-l) + 1)
    return maxx

def longestOnes2ndAproach(nums:[int], k: int) -> int:
    left = 0
    for right, n in enumerate(nums):
        if n == 0:
            k-=1
            
        if k<0:
            k += 1 - nums[left]
            left+=1
    return right-left+1
#        v
#0 1 0 0 1 1 0 1 0 1 1 1 1 0 2
#                        ^    
def longestOnes3rdAproach(nums:[int], k: int) -> int:
    l,zeros,maxx = 0,0,0

    for r,n in enumerate(nums):
        if n == 0:
            zeros += 1

        if zeros > k:
            zeros -= 1 - nums[l]
            l +=1
        elif zeros <= k:
             maxx = max(maxx, r - l +1)
    return maxx

@pytest.mark.parametrize('nums,k,output,expected',
                         [
                             ([1,1,1,0,0,0,1,1,1,1,0],2,6,True),
                             ([0,1,1,1,0,0,0,1,1,0,0,1,1,0],2,6,True),
                             ([0,1,1,1,0,0,0,1,1,0,0,1,1,0],3,8,True),
                             ([1,1,1,0,0,0,1,1,1,1,0],3,10,True),
                             ([0,1,0,0,1,1,0,1,0,1,1,1,1,0],2,9,True)
                          ])
def test_longestOnes3rdAproach(nums,k,output,expected):
    assert (longestOnes2ndAproach(nums,k) == output) == expected

