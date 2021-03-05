class Solution:
    def twoSum(self,nums,k):
        result=[]
        tmp_set=set()
        for i in nums:
            if -k-i in tmp_set:
                result.append(sorted([i,k,-k-i]))
            else:
                tmp_set.add(i)
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            result=result+self.twoSum(nums[:i]+nums[i+1:],nums[i])
        new_result=[list(t) for t in set([tuple(_) for _ in result])]
        return new_result
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l=i+1
            r=n-1
            while (l<r):
                if nums[i]+nums[l]+nums[r]==0:
                    result.append([nums[i],nums[l],nums[r]])
                    while l<r and (nums[l+1]==nums[l]):
                        l+=1
                    while l<r and (nums[r-1]==nums[r]):
                        r-=1
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return result