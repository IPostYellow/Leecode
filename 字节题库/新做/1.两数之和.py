class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set={}
        for i in range(len(nums)):
            if target-nums[i] in num_set:
                return [num_set[target-nums[i]],i]
            else:
                num_set[nums[i]]=i