#!/usr/bin/env Python
# coding=utf-8
'''
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，
总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
注意:
字符串长度 和 k 不会超过 104。
示例 1:
输入:
s = "ABAB", k = 2
输出:
4
解释:
用两个'A'替换为两个'B',反之亦然。
示例 2:
输入:
s = "AABABBA", k = 1
输出:
4
解释:
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
执行用时：144 ms, 在所有 Python3 提交中击败了61.25%的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了60.43%的用户
'''
from collections import defaultdict

#将窗口内的字母用dict记录下来，判断当前窗口的长度和字典里出现最多次数的字母的差是否小于k,如果小于k则说明还能继续滑动，否则将移动left
class Solution:
    def characterReplacement(self, s, k):
        maxLen, windowLeft, windowRight, maxWord = 0, 0, 0, 0
        wordDict = defaultdict(int)
        while windowRight < len(s):
            wordDict[s[windowRight]] += 1
            maxWord = max(wordDict[s[windowRight]], maxWord)
            if(windowRight-windowLeft+1-maxWord)>k:
                wordDict[s[windowLeft]]-=1
                windowLeft+=1
            maxLen=max(maxLen,windowRight-windowLeft+1)
            windowRight+=1
        return maxLen

s = Solution()
print(s.characterReplacement("ABBB", 2))
