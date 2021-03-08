class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_ok(s):
            cnt_num = 0
            for i in s:
                if i == "(":
                    cnt_num += 1
                elif i == ")":
                    cnt_num -= 1
                if cnt_num < 0:
                    return False
            return cnt_num == 0

        level = set()
        level.add(s)
        while True:
            ans = list(filter(is_ok, level))
            if ans:
                return ans
            else:
                next_level = set()
                for i in level:
                    for j in range(len(i)):
                        if i[j] in "()":
                            next_level.add(i[:j] + i[j + 1:])
            level = next_level