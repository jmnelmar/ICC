'''
Remove duplicates from a sorted array
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
'''
def removeDuplicates(nums) -> int:
    i = 0
    while i > len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del(nums[i])
        else:
            i += 1
    return len(nums)