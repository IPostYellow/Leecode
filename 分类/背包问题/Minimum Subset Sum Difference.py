"""
给定一组正数数组，将这个数组分成两个子集并且使得他们的差最小。
Example 1: #
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
Example 2: #
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
Example 3: #
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
"""
class A:
    def __init__(self):
        self.ans=float("inf")
    def track_back(self,num,used,set1,set2):
        if abs(set2-set1)<self.ans:
            self.ans=abs(set2-set1)
        for i in range(len(num)):
            if used[i]==0:
                used[i]=1
                self.track_back(num,used,set1+num[i],set2-num[i])
                used[i]=0

    def can_partition(self,num):
        self.track_back(num,[0 for _ in range(len(num))],0,sum(num))
        return self.ans

a=A()
print(a.can_partition([1,2,3,9]))
a=A()
print(a.can_partition([1,2,7,1,5]))
a=A()
print(a.can_partition([1,3,100,4]))