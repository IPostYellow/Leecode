from typing import List
class Solution:
    def __init__(self):
        self.result = []

    def track_back(self, nums, track, used):
        if len(nums) == len(track):
            self.result.append(track)
            return
        else:
            for i in range(len(nums)):
                if (i > 0) and (used[i - 1] == 1) and (nums[i - 1] == nums[i]):
                    continue
                if used[i] == 1:
                    continue
                else:
                    used[i] = 1
                    self.track_back(nums, track + [nums[i]], used)
                    used[i] = 0

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [0] * len(nums)
        self.track_back(nums, [], used)
        return self.result

s=Solution()
print(s.permuteUnique([1,1,2]))