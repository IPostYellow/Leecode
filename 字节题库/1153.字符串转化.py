'''
给出两个长度相同的字符串，分别是 str1 和 str2。请你帮忙判断字符串 str1 能不能在 零次 或 多次 转化后变成字符串 str2。
每一次转化时，将会一次性将 str1 中出现的 所有 相同字母变成其他 任何 小写英文字母（见示例）。
只有在字符串 str1 能够通过上述方式顺利转化为字符串 str2 时才能返回 True，否则返回 False。​​

示例 1：
输入：str1 = "aabcc", str2 = "ccdee"
输出：true
解释：将 'c' 变成 'e'，然后把 'b' 变成 'd'，接着再把 'a' 变成 'c'。注意，转化的顺序也很重要。
示例 2：
输入：str1 = "leetcode", str2 = "codeleet"
输出：false
解释：我们没有办法能够把 str1 转化为 str2。 

提示：
1 <= str1.length == str2.length <= 10^4
str1 和 str2 中都只会出现 小写英文字母
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-transforms-into-another-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str2 == str1:
            return True
        tmp = dict()
        exist = set()
        for i in range(len(str1)):
            if str1[i] not in tmp: #将转化后的字母存入tmp中，假设全部都转化为了另一个字母
                tmp[str1[i]] = str2[i]
                exist.add(str2[i])
            elif tmp[str1[i]] != str2[i]: #发现str1中相同的字母对应了str2中的不同的字母，则不可能转化成功
                return False
        if len(exist) >= 26:
            return False
        else:
            return True


class Solution2:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str2 == str1:
            return True
        l = set()
        for i in str2:
            l.add(i)
        if len(l) == 26:
            return False
        for i in range(len(str1)):
            for j in range(len(str1)):
                if str1[i] == str1[j]:  # 反过来思考不能转化的情况，只要出现了有冲突的数字，比如str1中有两个相同的字母对应str2中两个不同的字母。则不可能转化成功
                    if str2[i] != str2[j]:
                        return False
        return True
