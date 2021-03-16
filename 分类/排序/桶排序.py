def bucket_sort(nums):
    min_num=min(nums)
    max_num=max(nums)
    bucket_range=(max_num-min_num)/len(nums)

    count_list=[[] for _ in range(len(nums)+1)]

    for i in nums:
        count_list[int((i-min_num)//bucket_range)].append(i)
    nums.clear()
    for i in range(len(count_list)):
        for j in sorted(count_list[i]):
            nums.append(j)


nums=[3.2,6,8,4,2,6,7,3,3.1]
bucket_sort(nums)
print(nums)