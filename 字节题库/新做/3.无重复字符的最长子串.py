class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left,right=0,1
        max_len=1
        cur_dict=set(s[left])
        while right<len(s):
            if s[right] in cur_dict:
                if max_len<(right-left):
                    max_len=right-left
                cur_dict.discard(s[left])
                left+=1
            else:
                cur_dict.add(s[right])
                right+=1
        if (right-left)>max_len:
            max_len=right-left
        return max_len