from collections import Counter
def contains_duplicate(nums:list[int]) -> bool:
    map_nums = Counter(nums)

    for n in map_nums.keys():
        if map_nums[n] > 1:
            return True
    return False

a = [1,2,3,4,5,5,6,7]
print(contains_duplicate(a))
b = [1,2,3,4,5,6,7]
print(contains_duplicate(b))
