"""
给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

示例 1:

输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3。
示例 2:

输入: s = "aa", k = 1
输出: 2
解释: 则 T 为 "aa"，所以长度为 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s:
            return 0
        charnum=defaultdict(int)
        total_char=0
        left,right=0,0
        max_len=0
        while right<len(s):
            if s[right] not in charnum: # 滑动窗口右边
                total_char+=1
            charnum[s[right]]+=1
            while total_char>k: # 滑动窗口左边，维持窗口大小小于k
                charnum[s[left]]-=1
                if charnum[s[left]]==0:
                    total_char-=1
                    del charnum[s[left]]
                left+=1
            max_len=max(max_len,right-left+1) # 每次判断一下字符串长度
            right+=1
        return max_len

#第二次
from collections import defaultdict
class Solution2:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_len = 0
        char_cnt = 0
        char_Dict = defaultdict(int)
        while right < len(s):
            if s[right] not in char_Dict:
                char_cnt += 1
            char_Dict[s[right]] += 1

            while char_cnt > k:
                char_Dict[s[left]] -= 1
                if char_Dict[s[left]] == 0:
                    char_cnt -= 1
                    del char_Dict[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len