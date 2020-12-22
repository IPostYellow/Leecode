class Solution:
    def search(self, L, a, modulus, n, nums):
        h = 0
        for i in range(L):  # 计算一开始长度为L的编码值
            h = (h * a + nums[i]) % modulus
        seen = {h}
        aL = pow(a, L, modulus)  # a的L长度次方 也就是编码计算的时候最前面的一个数的次方+1，方便后面减去
        for start in range(1, n - L + 1):
            # 先乘a，使得h里的每个数的次方都+1，然后再减去最高的次方，再加后面一个值
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus  # 将h的编码的前面一个字符去掉，加后面一个字符
            if h in seen:
                return start #返回L长度重复子串的重复的开始点
            seen.add(h)
        return -1

    def longestDupSubstring(self, S):
        n = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(n)]  # 字符里的每个字母的26进制编码
        a = 26
        modulus = 1e9+7
        modulus=int(modulus)
        left, right = 1, n
        while left != right:
            L = left + (right - left) // 2
            if self.search(L, a, modulus, n, nums) != -1:
                left = L + 1
            else:
                right = L

        start = self.search(left - 1, a, modulus, n, nums)
        return S[start: start + left - 1] if start != -1 else ""


s = Solution()
print(s.longestDupSubstring("nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy"))


class Solution2:
    def search(self, midL, a, nums):
        h = 0
        for i in range(midL):
            h = (h * a + nums[i])
        tmp_result = set()
        tmp_result.add(h)
        al = a ** midL
        for i in range(1, len(nums) - midL + 1):
            h = (h * a - nums[i - 1] * al + nums[i + midL - 1])
            if h in tmp_result:
                return i
            tmp_result.add(h)
        return -1

    def longestDupSubstring(self, s: str) -> str:
        nums = [ord(i) - ord('a') for i in s]
        left, right = 1, len(s)
        # mods=int(1e9+7)
        while (left < right):
            mid = left + (right - left) // 2
            if self.search(mid, 26, nums) != -1:
                left = mid + 1
            else:
                right = mid

        result = self.search(left - 1, 26, nums)
        return s[result:result + left - 1] if result != -1 else ""