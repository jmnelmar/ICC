'''
55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element 
in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''
#recursive aproach
def canJump(nums: [int]) -> bool:

    goal = len(nums) - 1
    jumps = 0

    def jump(nums,i):
        if i >= len(nums) - 1:
            return 0 
        return jump(nums, i + nums[i]) + nums[i]
        
    jumps = jump(nums,0)
    print(jumps)
    if jumps >= goal:
        return True
    else:
        return False
#         v  
# 2,3,1,1,4
#greedy aproach to optimize paths and decisions
def canJumpGreedy(nums: [int]) -> bool:
    #initializing the goal
    goal = len(nums) - 1
    jumps = 0
    #going in backwards thru the array
    for i in range(len(nums) - 1, -1, -1):
        jumps = nums[i]
        #checking if i can afford the goal with the jumps + 1
        if i + jumps >= goal:
            #If I can afford update the goal to the i which should be the next jump
            goal = i
    #check if at the end we reach the final goal which should be traverse all the array from the end to the start
    if goal == 0:
        return True
    else:
        return False

def canJumpGame(nums:[int]) -> bool:
    goal = len(nums) - 1
    jumps = 0
    i = 0
    while jumps < goal:
        if nums[i] == 0 or nums[i] + i == 0:
            break 
        jumps = i + nums[i]
        print(f"i:{i},nums[{i}]:{nums[i]}, jumps:{jumps}")
        i = jumps
    
    if jumps >= goal:
        return True
    else:
        return False

    

nums = [2,3,1,1,4]
#nums = [3,2,1,-3,4]
print(canJumpGreedy(nums))
        
         
