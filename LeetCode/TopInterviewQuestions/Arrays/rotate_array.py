'''
Rotate an Array
leet code problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

def rotate( nums: list, k: int) -> None:
    chunk = nums[k*-1:]
    #chunk = chunk[::-1]
    rotations = 0
    if k > len(nums):
        rotations = (int)(k / len(nums))
    else:
        rotations = k
        
    result = []
    for i in range(k):
        result.append(chunk[i])
    for i in range(len(nums) -k):
        result.append(nums[i])
    
    nums = result
    print(nums)

def rotateII(nums:list, key:int):
    cnums = nums[:]
    lenn = len(nums)

    for i in range(lenn):
        nums[(i+k) % lenn] = cnums[i]



nums = [1,2,3,4,5,6,7] 
k = 3
rotateII(nums,k)
print(nums)
