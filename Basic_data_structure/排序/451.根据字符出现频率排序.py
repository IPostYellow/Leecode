'''
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
示例 1:
输入:
"tree"
输出:
"eert"
解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:
输入:
"cccaaa"
输出:
"cccaaa"
解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:
输入:
"Aabb"
输出:
"bbAa"
解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-characters-by-frequency
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import defaultdict
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        sort_result = sorted(d.items(), key=lambda item: item[1], reverse=True)
        # print(sort_result[::-1])
        # print(sort_result)
        new_s = ""
        for i in sort_result:
            for _ in range(i[1]):
                new_s += i[0]
        return new_s

    def frequencySort2(self, s):
        s = Counter(s).most_common()
        return ''.join([i * j for i, j in s])

    def frequencySort3(self, s):
        ret = []
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        bucket = [[] for _ in range(len(s) + 1)]
        for i in d:
            bucket[d[i]] += i * d[i]
        for i in bucket[::-1]:
            if i != []:
                ret += i
        return ''.join(ret)

s = Solution()
print(s.frequencySort3("tree"))
