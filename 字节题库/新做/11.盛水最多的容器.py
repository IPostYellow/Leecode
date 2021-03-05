class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        dp=[]
        res=0
        while(left<right):
            cur_water=(right-left)*min(height[left],height[right])
            if res<cur_water:
                res=cur_water
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res