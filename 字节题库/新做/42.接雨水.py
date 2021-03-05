class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left_max=[height[i] for i in range(n)]
        right_max=[height[i] for i in range(n)]
        for i in range(1,n):
            left_max[i]=max(left_max[i-1],left_max[i])
        for j in range(n-2,-1,-1):
            right_max[j]=max(right_max[j+1],right_max[j])
        sum=0
        for i in range(1,n-1):
            sum+=min(left_max[i],right_max[i])-height[i]
        return sum