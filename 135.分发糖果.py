from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        give=[0]*len(ratings)
        give[0]=1
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                give[i]=give[i-1]+1
            else:
                give[i]=1
        give2=[0]*len(ratings)
        give2[-1]=1
        for j in range(len(ratings)-2,-1,-1):
            if ratings[j]>ratings[j+1]:
                give2[j]=give2[j+1]+1
            else:
                give2[j]=1
        for i in range(len(give)):
            give[i]=max(give[i],give2[i])
        return sum(give)