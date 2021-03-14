"""
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
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_Dcit = defaultdict(int)
        left, right = 0, 0
        max_len = 0
        while right < len(s):
            char_Dcit[s[right]] += 1

            while (char_Dcit[s[right]] > 1):
                char_Dcit[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len

# 第二次
from collections import defaultdict


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 典型滑动窗口 使用哈希表记录遇到的字母
        max_len = 0
        left, right = 0, 0
        word_hash = collections.defaultdict(int)
        while right < len(s):
            word_hash[s[right]] += 1
            while word_hash[s[right]] > 1:
                word_hash[s[left]] -= 1
                if word_hash[s[left]] == 0:
                    del word_hash[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len