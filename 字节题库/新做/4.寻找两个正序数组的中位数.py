class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s1=0
        s2=0
        m=len(nums1)
        n=len(nums2)
        prev_num=-1
        cur_num=-1
        mid=(m+n)//2
        while(s1+s2<=mid):
            prev_num=cur_num
            if (s1<m) and ((s2>=n)or (nums1[s1]<nums2[s2])):
                cur_num=nums1[s1]
                s1+=1
            elif (s2<n) and ((s1>=m)or(nums2[s2]<=nums1[s1])):
                cur_num=nums2[s2]
                s2+=1
        if (m+n)%2==0:
            return (prev_num+cur_num)/2.0
        else:
            return float(cur_num)