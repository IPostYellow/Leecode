'''
在一排树中，第 i 棵树产生 tree[i] 型的水果。
你可以从你选择的任何树开始，然后重复执行以下步骤：

把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。

用这个程序你能收集的水果树的最大总量是多少？

 

示例 1：

输入：[1,2,1]
输出：3
解释：我们可以收集 [1,2,1]。
示例 2：

输入：[0,1,2,2]
输出：3
解释：我们可以收集 [1,2,2]
如果我们从第一棵树开始，我们将只能收集到 [0, 1]。
示例 3：

输入：[1,2,3,2,2]
输出：4
解释：我们可以收集 [2,3,2,2]
如果我们从第一棵树开始，我们将只能收集到 [1, 2]。
示例 4：

输入：[3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：我们可以收集 [1,2,1,1,2]
如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 棵水果树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fruit-into-baskets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import defaultdict
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # 和至多k个不同字符的最长子串题目类似 这就相当于至多包含2个不同数字的最长子数组
        left,right=0,0
        max_len=0
        fruit_cnt=0
        fruit_num=defaultdict(int)
        while right<len(tree):
            if tree[right] not in fruit_num:
                fruit_cnt+=1
            fruit_num[tree[right]]+=1
            while fruit_cnt>2: # 维护窗口大小小于2
                fruit_num[tree[left]]-=1
                if fruit_num[tree[left]]==0:
                    fruit_cnt-=1
                    del fruit_num[tree[left]]
                left+=1
            max_len=max(max_len,right-left+1)
            right+=1 # 窗口滑动
        return max_len

#第二次
from collections import defaultdict


class Solution2:
    def totalFruit(self, tree: List[int]) -> int:
        # 相当于问最多不超过2个数字的子串有多长
        left, right = 0, 0
        max_len = 0
        char_dict = defaultdict(int)
        fruit_cnt = 0
        while right < len(tree):
            if tree[right] not in char_dict:
                fruit_cnt += 1
            char_dict[tree[right]] += 1
            while fruit_cnt > 2:
                char_dict[tree[left]] -= 1
                if char_dict[tree[left]] == 0:
                    fruit_cnt -= 1
                    del char_dict[tree[left]]
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len