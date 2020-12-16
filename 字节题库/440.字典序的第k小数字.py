'''
给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。
注意：1 ≤ k ≤ n ≤ 109。
示例 :
输入:
n: 13   k: 2
输出:
10
解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_all_node(pre, n):
            cur = pre
            next = pre + 1
            count = 0
            while (cur <= n):
                count += min(n + 1, next) - cur
                cur *= 10
                next *= 10
            return count

        p = 1
        pre = 1
        while (p < k):
            cur_count = count_all_node(pre, n)
            if (p + cur_count > k):
                p += 1
                pre *= 10
            else:
                p+=cur_count
                pre+=1

        return pre
        # def get_all_nodes(prefix,n): #计算前缀下的所有结点数
        #     cur=prefix #当前前缀
        #     next=prefix+1 #下一个前缀
        #     count=0
        #     while(cur<=n):
        #         count+=min(n+1,next)-cur #计算所有结点
        #         cur=cur*10
        #         next=next*10
        #     return count
        # p=1 #作为一个指针，指向当前的位置，当p==k的时候说明结束了
        # prefix=1 #树前缀
        # while(p<k):
        #     count=get_all_nodes(prefix,n) #获取树的当前节点下的所有子节点数
        #     if (p+count>k): #当前节点+当前前缀所有子节点数要是大于k，则说明第k个数在这个前缀里
        #         prefix=prefix*10 #1变成10，也就是再下一个前缀
        #         p+=1 #指针+1，指向下一个数了
        #     elif (p+count<=k): #当前节点+当前前缀所有子节点数要是小于k，说明第k个数字不在这个前缀里，去下一个前缀
        #         prefix+=1 # 1变成2
        #         p+=count # 指针直接指过前一个前缀的所有结点
        # return prefix