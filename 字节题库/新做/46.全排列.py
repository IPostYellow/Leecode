class Solution:
    def __init__(self):
        self.result=[]
    def trackback(self,tmp,choose_list,rest):
        if rest==0:
            self.result.append(tmp)
        else:
            for i in range(len(choose_list)):
                self.trackback(tmp+[choose_list[i]],choose_list[:i]+choose_list[i+1:],rest-1)

    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        self.trackback([],nums,n)
        return self.result