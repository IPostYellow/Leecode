class Solution:
    def __init__(self):
        self.result=[]
    def trackback(self,nums,start,track):
        self.result.append(track)
        for i in range(start,len(nums)):
            self.trackback(nums,i+1,track+[nums[i]])
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.trackback(nums,0,[])
        return self.result