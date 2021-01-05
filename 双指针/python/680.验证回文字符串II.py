'''
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
示例 1:
输入: "aba"
输出: True
示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
'''
class Solution:
    def reverse(self,s_list,rest_chance):
        left,right=0,len(s_list)-1
        while(left<right):
            if s_list[left]==s_list[right]:
                left+=1
                right-=1
            elif rest_chance>0:
                l=self.reverse(s_list[left+1:right+1],rest_chance-1)
                r=self.reverse(s_list[left:right],rest_chance-1)
                return l or r
            else:
                return False
        return True
    def validPalindrome(self, s: str) -> bool:
        return self.reverse(list(s),1)