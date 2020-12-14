from typing import List


class Solution:
    def reverseString1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]
    def reverseString3(self, s: List[str]) -> None:
        left,right=0,len(s)-1
        while(left<right):
            tmp=s[left]
            s[left]=s[right]
            s[right]=tmp
            left+=1
            right-=1

    def reversestring4(self,s):
        def dfs(s, start, end):
            if start > end:
                return
            dfs(s, start + 1, end - 1)
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
        dfs(s,0,len(s)-1)

