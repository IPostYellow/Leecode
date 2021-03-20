"""
给定一串字符串。找出其字母大小写的子集
比如：
Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""


def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)
    for i in range(len(str)):
        n = len(permutations)
        if str[i].isalpha():
            for j in range(n):
                tmp = list(permutations[j])
                tmp[i] = tmp[i].swapcase()
                permutations.append("".join(tmp))

    return permutations


def find_letter_case_string_permutations2(str):
    permutations = [""]
    for i in range(len(str)):
        n = len(permutations)
        if str[i].isalpha():
            for j in range(n):
                tmp = list(permutations[j])
                tmp.append(str[i])
                permutations.append("".join(tmp))
                permutations[j]+=str[i].swapcase()
        else:
            for j in range(n):
                permutations[j]+=str[i]
    return permutations


print(find_letter_case_string_permutations2("ad52"))
print(find_letter_case_string_permutations2("ab7c"))
