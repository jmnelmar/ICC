nums = [0,1,0,3,12]

def movezeros(nums):
    indexs = []

    for i in range(nums):
        if nums[i] == 0:
            indexs.append(i)
        for i in range(len(indexs)):
            nums.pop(nums[i] - i)
            nums.append(0)

movezeros(nums)
print(nums)