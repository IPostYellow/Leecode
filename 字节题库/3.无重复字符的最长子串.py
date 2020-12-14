'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:
输入: s = ""
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import defaultdict


class Solution:#80ms,13.6mb
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = defaultdict(int)
        p1, p2 = 0, 0
        max_len = 0
        while (p1 <= p2 and p2 < len(s)):
            if tmp[s[p2]] == 1:
                if max_len < p2 - p1:
                    max_len = p2 - p1
                tmp[s[p1]] -= 1
                p1 += 1
            else:
                tmp[s[p2]] = 1
                p2 += 1
        if p2 - p1 > max_len:
            max_len = p2 - p1
        return max_len

s=Solution()
print(s.lengthOfLongestSubstring(''))

#第二次写
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        a=set()
        max_len=0
        while(right<len(s)):
            if s[right] in a:
                if max_len<right-left:
                    max_len=right-left
                a.remove(s[left])
                left+=1
            else:
                a.add(s[right])
                right+=1
        if right-left>max_len:
            max_len=right-left
        return max_len
