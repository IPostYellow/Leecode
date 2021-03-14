def count_sort(nums): # 无法处理小数
    min_num=min(nums)
    max_num=max(nums)
    count_list=[0]*(max_num-min_num+1)
    for i in nums:
        count_list[i-min_num]+=1
    nums.clear()
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            nums.append(i+min_num)


nums=[3,6,8,1,4,1,2,6]
count_sort(nums)
print(nums)
