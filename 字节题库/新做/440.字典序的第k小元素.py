class Solution:
    def compute_count(self,pre,n):# pre树下有多少个节点
        cur=pre
        next=pre+1
        count=0
        while(cur<=n):
            count+=min(n+1,next)-cur #pre这一层有多少节点
            cur*=10 #去下一层
            next*=10
        return count
    def findKthNumber(self, n: int, k: int) -> int:
        cur_count=1
        pre=1
        while(cur_count<k):
            count=self.compute_count(pre,n)
            if cur_count+count<k:
                cur_count+=count
                pre+=1
            elif cur_count+count==k: # 加完pre这一层的刚好够，那pre+1下一个就是了
                return pre+1
            else:
                cur_count+=1 # 去掉了pre这个点
                pre*=10
        return pre