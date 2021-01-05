'''
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
示例 1：
输入："hello"
输出："holle"
示例 2：
输入："leetcode"
输出："leotcede"

提示：
元音字母不包含字母 "y" 。
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        ss=list(s)
        dig= {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left,right=0,len(s)-1
        while(left<right):
            if ss[left] in dig and ss[right] in dig:
                tmp=ss[left]
                ss[left]=ss[right]
                ss[right]=tmp
                left+=1
                right-=1
            elif ss[left] in dig and ss[right] not in dig:
                right-=1
            elif ss[left] not in dig and ss[right] in dig:
                left+=1
            else:
                left+=1
                right-=1
        return ''.join(ss)