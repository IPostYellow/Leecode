"""
给定一个数字N，找出N对括号的合法表达式
Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
Input: N=2
Output: (()), ()()
"""
from collections import deque


class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount


def generate_valid_parentheses(num):
    """借助队列，出队元素的括号数要是满足N对括号，则添加至答案中，否则就判断左括号的数量，如果左括号的数量比N小，则可以继续加左括号，如果左括号比右括号多，则可以添加右括号"""
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        tmp = queue.popleft()
        if tmp.openCount == num and tmp.closeCount == num:  # 找到答案
            result.append(tmp.str)
        else:
            if tmp.openCount < num:  # 继续添加左括号
                queue.append(ParenthesesString(tmp.str + "(", tmp.openCount + 1, tmp.closeCount))
            if tmp.openCount > tmp.closeCount:  # 如果左括号比右括号多，则可以继续添加右括号
                queue.append(ParenthesesString(tmp.str + ")", tmp.openCount, tmp.closeCount + 1))
    return result


def generate_valid_parentheses2(num):
    result = []
    que = deque()
    que.append(["", 0, 0])
    while que:
        tmp = que.popleft()
        if tmp[1] == num and tmp[2] == num:
            result.append(tmp[0])
        else:
            if tmp[1] < num:
                que.append([tmp[0] + "(", tmp[1] + 1, tmp[2]])
            if tmp[1] > tmp[2]:
                que.append([tmp[0] + ")", tmp[1], tmp[2] + 1])
    return result


print(generate_valid_parentheses(2))
print(generate_valid_parentheses(3))

print(generate_valid_parentheses2(2))
print(generate_valid_parentheses2(3))
