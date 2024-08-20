def roate_k_times(nums:list, k:int):
    cnums = nums[:]
    lenn = len(nums)

    for i in range(lenn):
        nums[(i + k) % lenn] = cnums[i]
    
    


a = [1,2,3,4,5,6,7]
k = 3
print(a)
roate_k_times(a,k)
print(a)