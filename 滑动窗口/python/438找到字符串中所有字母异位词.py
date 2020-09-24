# coding=utf-8
'''
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import defaultdict


class Solution:#188ms,14.4MB
    def check(self, s_dict, p_dict):
        for i in p_dict:
            if s_dict[i] != p_dict[i]:
                return False
        return True

    def findAnagrams(self, s, p):
        if len(s)<len(p):
            return []
        s_dict = defaultdict(int)
        p_dict = defaultdict(int)
        result = []
        left,right=0,-1
        for i in p:
            p_dict[i] += 1
        for i in range(len(p)):
            right+=1
            if s[right] in p_dict:
                s_dict[s[right]]+=1
        while right<len(s):
            if (self.check(s_dict,p_dict)):
                result.append(left)
            if s[left] in p_dict:
                s_dict[s[left]] -= 1
            left+=1
            right+=1
            if right<len(s) and s[right] in p_dict:
                s_dict[s[right]]+=1
        return result


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
