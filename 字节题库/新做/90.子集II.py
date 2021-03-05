class Solution:
    def __init__(self):
        self.result=[]
    def trackback(self,nums,start,track):
        self.result.append(track)
        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            else:
                self.trackback(nums,i+1,track+[nums[i]])

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.trackback(nums,0,[])
        return self.result