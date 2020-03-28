"""
插入排序的空间复杂度O(1),时间复杂度O(N^2),稳定排序算法（稳定是指若两个都排在同一个位置）
那么之前是怎样一个先后顺序，之后还是怎样
初级排序算法包括插入，选择，冒泡 排序
"""
nums=[5,3,6,4,1,2,8,7]
for i in range(1,len(nums)):
    for j in range(i):
        #j 在i之前
        if nums[j]>nums[i]:
            ins=nums[i]
            nums.pop(i)
            nums.insert(j,ins)
            break

print(nums)