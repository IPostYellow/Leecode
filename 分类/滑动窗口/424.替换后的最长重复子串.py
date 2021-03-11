"""
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 104。

 

示例 1：

输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。
示例 2：

输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 找到窗口内出现最多次数的字符，若当前窗口的字符数-出现最多次数的字符>k，则开始滑动窗口左边
        left,right=0,0
        max_len=0
        char_dict=defaultdict(int)
        max_word=0
        while right<len(s):
            char_dict[s[right]]+=1
            max_word=max(max_word,char_dict[s[right]])
            if (right-left+1-max_word)>k: #当前滑动窗口的值可以不维护，因为如果后面要出现更长的子串的话，就必须大过max_word+k，才行。
                char_dict[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
            right+=1
        return max_len

#第二次
from collections import defaultdict
class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_len, most_word = 0, 0
        word_count = defaultdict(int)
        while (right < len(s)):
            word_count[s[right]] += 1
            most_word = max(most_word, word_count[s[right]])

            while right - left + 1 - most_word > k:  # 不需要维护most_word,因为后面的长度要想更长，most_word必须大于当前才行，因为长度是most_word+k，k是不变的
                word_count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len