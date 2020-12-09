### 基础数据结构相关操作
## 栈
[带有最小值的栈(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/%E5%8C%85%E5%90%AB%E6%9C%80%E5%B0%8F%E5%80%BC%E7%9A%84%E6%A0%88.py)<br>
## 链表
[反转链表(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py)<br>
[判断链表是否有环(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/141%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8.py)<br>
[判断链表中环的入口(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/142%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.py)<br>
[删除链表中给定的节点(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/237%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.py)<br>
[反转链表的一部分(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/92%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A82.py)<br>
[链表的中间结点(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/876%E9%93%BE%E8%A1%A8%E7%9A%84%E4%B8%AD%E9%97%B4%E7%BB%93%E7%82%B9.py)<br>
[合并两个有序链表(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/21%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8.py)<br>
[链表分割(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/86%E5%88%86%E9%9A%94%E9%93%BE%E8%A1%A8.py)<br>
[删除链表的倒数第n个结点(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/19%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E7%BB%93%E7%82%B9.py)<br>
## 树
[二叉树的后序遍历(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/145%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86.py)<br>

## 排序
[链表归并排序(python)](https://github.com/IPostYellow/Leecode/blob/master/Basic_data_structure/%E6%8E%92%E5%BA%8F/148%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8.py)<br>
### 记录Leetcode刷的题目
Python版本、Java版本（尚未完成）<br>
按分类查看：[滑动窗口](#滑动窗口)、[二分搜索](#二分搜索)、[动态规划](#动态规划)、[回溯法](#回溯法)<br>

## 滑动窗口
解题模板：<br>
```
windowSize=看求最大还是最小，根据不同的题目设置个初始值
left,right=0<br>
while (right<len(待滑动的列表/字符串)):
    对当前right位置的元素进行操作
    while(满足了缩小窗口的条件):
        缩小窗口(更新left的值)
    扩大窗口(更新right的值)
```
<br>

[209.长度最小的子数组(Python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3/python/209%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.py)<br>
思路：创建一个滑动窗口和窗口尺寸，right指针不断向右移，并记录下窗口内的值的总和，如果大于等于给定的值，则判断窗口大小是否比上一次的小，如果小则更新最小窗口大小，并且不断移动left指针缩小窗口，直到窗口内总和小于给定的值为止，每移动一次left指针，再判断一次窗口内总和是否大于等于给定的值而且窗口大小是否比当前最小窗口大小小，如果是则更新最小窗口大小，否则就继续。直到right指针移动过最右边为止。消耗时间44ms,消耗内存15.2MB。对应的模板中的例子就是：<br>
```
windowSize=给定的数组长度+1
当前窗口内的值总和=0
left,right=0
while (right<len(待滑动的列表/字符串)):
    将当前的值加入到窗口总和去
    while(当前的窗口内的值总和大于等于给定的阈值s):
        缩小窗口(更新left的值)
    扩大窗口(更新right的值)
```
<br>

[424.替换后的最长重复字符(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3/python/424%E6%9B%BF%E6%8D%A2%E5%90%8E%E7%9A%84%E6%9C%80%E9%95%BF%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6.py)<br>
思路：将窗口内的字母用哈希表记录下来，判断当前窗口的长度与哈希表中最多的字母数的差是否小于给定的k值，如果小于k值说明窗口还可以继续，否则说明需要移动窗口了，将窗口的左边界移动。消耗时间144ms,消耗内存13.4MB。对应的模板中的例子就是：<br>
```
窗口内字母哈希表初始化
最大窗口=0
窗口内相同字母最多的个数=0
left,right=0
while (right<len(待滑动的列表/字符串)): 
    将当前的字母记录到哈希表中去，并更新窗口内相同字母最多的个数
    while(当前窗口的长度与哈希表中最多的字母数的差大于给定的k值):
        将哈希表中left指向的字母个数减1，缩小窗口(更新left的值)
    判断当前窗口大小和历史最大窗口，看看是否要更新最大窗口大小
    扩大窗口(更新right的值)
```
<br>

[438.找到字符串中所有字母异位词(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3/python/438%E6%89%BE%E5%88%B0%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E6%89%80%E6%9C%89%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D.py)<br>
思路：固定滑动窗口的大小为所找字符的长度。然后不断判断窗口内的每种字母的个数是否和所找字符中每种字母的个数相等。若相等则说明该窗口的起始位置为答案之一，否则滑动窗口。消耗时间188ms,消耗内存14.4MB。对应的模板中的例子就是：<br>
```
s_dict=defaultdict(int)#滑动窗口内每种字母个数的字典
p_dict=defaultdict(int)#所找字符串每种字母个数的字典
left,right=0,-1
for i in p:#构建所找字符串中每种字母的个数字典
    p_dict[i]+=1
for i in range(len(p)):#移动右指针使得窗口和所找字符串长度相等
    right+=1
    if s[right] in p_dict:
        s_dict[s[right]]+=1
while right<len(s)：
    if(当前窗口内每种字母的个数和所找字符串中每种字母个数相等):
        得到答案，将此答案存起来
    if(s[left] in p_dict):
        将存储的窗口内最左边的有效值的字典值-1
    left+=1#移动窗口
    right+=1
    if right<len(s) and s[right] in p_dict:#移动窗口后把是所找字符串内的字母给加到当前的滑动窗口内每种字母个数的字典中去
        s_dict[s[right]]+=1
return 总答案
```

## 二分搜索
解题模板：<br>
```
def binarySearch(nums,target):
    left,right=0,len(nums)或者len(nums)-1
    while(left<right或者left<=right):
        mid = left +(right-left)>>1
        if (nums[mid]==target):
            找到了答案
        elif (nums[mid]<target): #答案在右边的区间
            left=mid或者mid-1
        elif (nums[mid]>target): #答案在左边的区间
            right=mid+1或者mid
    return 搜索失败
```
<br>

[33.旋转排序数组(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/33%E6%90%9C%E7%B4%A2%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84.py)<br>
思路：搜索区间为[left,right]，最终要找到区间没有元素为止，所以while里面的判断条件是left<=right。这种改变了有序的条件的数组，首先要判断mid到底在哪边，因为mid肯定是在旋转产生的两个有序数组中的某一个之中。如果mid的元素比left的大，说明left在mid都是递增的，否则说明mid到right是递增的。然后再判断二分搜索的下一个区间。
```
def search(self, nums, target):
    left, right = 0, len(nums) - 1
    while (left <= right):
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        if nums[mid] >= nums[left]:  # 判断mid位置是在递增序列上还是在先递增后递减的序列上
            if nums[left] <= target < nums[mid]:  
            # 如果是在递增序列上，left到mid是递增的，那么我们判断目标是否在这个递增区间内，如果在就取这个区间，否则则取右边的区间
                right = mid - 1
            else:
                left = mid + 1
        else: 
        #如果不是在递增序列上，则说明mid到right是递增的，那么我们判断目标是否在这个递增区间内，如果在就取这个区间，否则就取左边的区间
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

[81.搜索旋转排序数组II(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/81%E6%90%9C%E7%B4%A2%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84II.py)<br>
思路：和[33.旋转排序数组]是一类题目，思路是一致的，只不过要返回True和False而已。
```
def search(self, nums, target):
    left, right = 0, len(nums) - 1
    while (left <= right):
        mid = (left + right) // 2
        if target == nums[mid]:
            return True
        if nums[left] < nums[mid]:
            if (nums[left] <= target < nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        elif nums[left] == nums[mid]:
            left=left+1
        else:
            if (nums[mid] < target <= nums[right]):
                left = mid + 1
            else:
                right = mid - 1
    return False
```

[34.在排序数组中查找元素的第一个最后一个位置(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/34%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E6%9F%A5%E6%89%BE%E5%85%83%E7%B4%A0%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%92%8C%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E4%BD%8D%E7%BD%AE.py)<br>
思路：和基本的二分搜索差不多，只不过找到了答案还不能直接返回，如果要找到第一个位置，找到了答案还必须搜寻他的左区间，如果找最后一个位置，找到了答案还必须搜索他的右区间。
```
def searchRange(self, nums: List[int], target: int) -> List[int]:
    leftans, rightans = -1, -1 #初始化答案为-1，-1
    left, right = 0, len(nums) - 1 
    while (left <= right):
        mid = left + ((right - left) >> 1)
        if (nums[mid] == target): 
            leftans = mid
            right = mid - 1
        elif (nums[mid] < target):
            left = mid + 1
        elif (nums[mid] > target):
            right = mid - 1
    left, right = 0, len(nums) - 1
    while (left <= right):
        mid = left + ((right - left) >> 1)
        if (nums[mid] == target):
            rightans = mid
            left = mid + 1
        elif (nums[mid] < target):
            left = mid + 1
        elif (nums[mid] > target):
            right = mid - 1
    return [leftans, rightans]
```

[153.寻找旋转排序数组中的最小值(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/153%E5%AF%BB%E6%89%BE%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9C%80%E5%B0%8F%E5%80%BC.py)<br>
思路：因为要在[left,right]中搜索，所以right=len(nums)-1，最终我们要留下那个最小值，所以区间到最后还有一个元素，所以while中left<right。然后对于数组[3,4,5,6,7,0,1,2]，有那么一些情况，如果mid值比left和right的值都要小，类似mid=0,mid=1，则说明最小值在[left,mid]中。如果mid值比left和right的值都要大，比如mid=4,5,6,7，则说明最小值在(mid,right]中。而对于没有旋转的数组[0,1,2,3,4,5,6,7],mid的值肯定是大于left的值小于right的值的，此时的最小值也在[left,mid]中。把两种[left,mid]的情况合并，得出只要mid的值大于right的值的时候应该去(mid,right]区间搜寻，其他情况都应该在[left,mid]中搜寻。
```
def findMin(self, nums: List[int]) -> int:
    left,right=0,len(nums)-1
    while(left<right):
        mid=left+((right-left)>>1)
        if nums[mid]>nums[right]:
            left=mid+1
        else:
            right=mid
    return nums[left]
```

[154.寻找旋转排序数组中的最小值II(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/154%E5%AF%BB%E6%89%BE%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9C%80%E5%B0%8F%E5%80%BCII.py)<br>
思路：和[153.寻找旋转排序数组中的最小值]的思路类似，只不过在153中讨论的三种情况中，多了一种mid的值等于right的值的情况，这种时候我们只需要将right的值减一即可。相当于去除重复元素。
```
def findMin(self, nums: List[int]) -> int:
    left,right=0,len(nums)-1
    while(left<right):
        mid=left+((right-left)>>1)
        if nums[mid]>nums[right]:
            left=mid+1
        elif nums[mid]<nums[right]:
            right=mid
        else:
            right-=1
    return nums[left]
```

[852.山脉数组的峰顶索引(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/852%E5%B1%B1%E8%84%89%E6%95%B0%E7%BB%84%E7%9A%84%E5%B3%B0%E9%A1%B6%E7%B4%A2%E5%BC%95.py)<br>
思路：等价于找数组中的极大值，可以直接遍历然后判断如果前一个元素大于他后面的元素则说明找到了答案。也可以使用二分搜索。因为山峰的特点，在山顶左边是递增的，山顶右边是递减的，所以在二分搜索的时候判断是递增还是递减就可以知道该向哪半边进行二分搜索。
```
        left, right = 0, len(arr) - 1
        while (left < right):
            mid = (right - right) // 2 + left
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
```

[1283.使结果不超过阈值的最小除数(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/1283%E4%BD%BF%E7%BB%93%E6%9E%9C%E4%B8%8D%E8%B6%85%E8%BF%87%E9%98%88%E5%80%BC%E7%9A%84%E6%9C%80%E5%B0%8F%E9%99%A4%E6%95%B0.py)<br>
思路：利用值域的二分实现二分搜索，很显然除数的范围在1~数组里最大值之间取得。所以left和right开始的取值为1和max(nums)。如果mid的结果不比阈值大，说明这个除数还可以再小一点，所以可以继续搜索[1,mid-1]内的除数。如果mid的结果比阈值大，说明除数太小了，必须加大，所以要搜寻[mid+1,right]之间的除数。
```
def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    left, right = 1, max(nums)
    ans = -1
    def res_sum(p, nums):
        return sum([math.ceil(i / p) for i in nums])
    while (left <= right):
        mid = left + (right - left >> 1)
        if res_sum(mid, nums) <= threshold:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
```

[875.爱吃香蕉的珂珂(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/875%E7%88%B1%E5%90%83%E9%A6%99%E8%95%89%E7%9A%84%E7%8F%82%E7%8F%82.py)<br>
思路：思路上和[1283.使结果不超过阈值的最小除数]类似，就是要找到一个除数K。那么也可以用1283中的方法进行二分查找。
```
def minEatingSpeed(self, piles: List[int], H: int) -> int:
    left,right=1,max(piles)
    ans=-1
    def eat_time(K,piles):
        return sum([math.ceil(i/K) for i in piles])
    while(left<=right):
        mid=left+(right-left>>1)
        if (eat_time(mid,piles)<=H):
            ans=mid
            right=mid-1
        else:
            left=mid+1
    return ans
```

[162.寻找峰值(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/162%E5%AF%BB%E6%89%BE%E5%B3%B0%E5%80%BC.py)<br>
思路：我们可以画出带峰值的曲线观察规律，由于nums[-1]=nums[n]=负无穷。所以这个曲线肯定是两端下降的。那么对于一个mid值，可能存在四种情况。1.左<mid<右，这个时候峰值在右边区间。2.左>mid>右，这个时候峰值在左边。3.左>mid而且右>mid，这种情况左右皆有峰值。4.mid>左且mid>右，mid就是答案。其中第三种答案可以并到前面两种答案之中，本文代码以右判断为例。
```
def findPeakElement(self, nums: List[int]) -> int:
    if len(nums) <= 3:
        return nums.index(max(nums))
    left, right = 0, len(nums) - 1
    while (left < right): # 如果是边界的值，最后是要留下一个数作为峰值的
        mid = left + (right - left >> 1)
        if (nums[mid + 1] < nums[mid] and nums[mid] > nums[mid - 1]): #找到了答案
            return mid
        elif (nums[mid + 1] > nums[mid]): # 右边更大，说明峰值在右边
            left = mid + 1
        elif (nums[mid + 1] < nums[mid]): # 左边更大，说明峰值在左边
            right = mid - 1
    return left
```

[287.寻找重复数(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/287%E5%AF%BB%E6%89%BE%E9%87%8D%E5%A4%8D%E6%95%B0.py)<br>
思路：对值域进行二分搜索，因为数组长度为n+1，而里面的值是1到n，而且已知必然有一个数字重复出现。那么如果从1到n中取出一个mid值，然后判断数组中小于等于mid值的元素个数，如果小于等于mid值的元素个数大于了mid值，说明里面包含了重复元素，则下一次搜索应该在[1,mid]中，否则应该到(mid,n]中。
```
def findDuplicate(self, nums: List[int]) -> int:
    left,right=1,len(nums)-1
    def low_num(nums,p):
        res=0
        for i in nums:
            if i<=p:
                res+=1
        return res
    while(left<right):
        mid=left+(right-left>>1)
        if (low_num(nums,mid)>mid):
            right=mid
        else:
            left=mid+1
    return left
```

## 动态规划
解题模板：<br>
```
dp=初始化条件 #一般是个多维数组
for 状态1 in 状态1的所有可能取值:
	for 状态2 in 状态2所有可能的取值
    	搞不好还得for
        dp[状态1][状态2]=递推式
```
<br>

[509.斐波那契数(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/509%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.py)<br>
思路：由斐波那契数的定义可以知道，f[0]=0,f[1]=1,f[i]=f[i-1]+f[i-2](i>=2)。这个完美符合动态规划的特征，所以直接令dp=[0 for i in range(N + 1)],dp[1]=1，然后dp[N]=dp[N-1]+dp[N-2],从1开始递推到dp[N]即可。
```
def fib(self, N: int) -> int:
    if N <= 1:
        return N
    dp = [0 for i in range(N + 1)]
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]
```

[322.零钱兑换(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/322.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2.py)<br>
思路：如果设f[n]为金钱总数为n所需要的最少硬币数，如果硬币的面额有[1,2,5],则f[n]=min(f[n-1]+1,f[n-2]+1,f[n-5]+1)。如果n-硬币面额小于0的话，则不考虑。f[0]很显然为0，因为金钱总数为0的最少硬币数肯定是0。初始化所有f[i](i<=n)为-1，然后迭代将满足递推的所有f计算出来，最后返回f[n]。
```
def coinChange(self, coins: List[int], amount: int) -> int:
    f = [-1 for i in range(amount + 1)]
    f[0] = 0
    for i in range(1, amount + 1):
        tmp = []
        for j in coins:
            if i - j >= 0 and f[i - j] != -1:
                tmp.append(f[i - j])
        if tmp == []:
            f[i] = -1
        else:
            f[i] = min(tmp) + 1
    return f[amount]
```

<br>
另外，此题也可以用回溯法。根据回溯法的模板也可以写出如下程序，但是在LeetCode上会超时。
<br>

```
def coinChange(self, coins: List[int], amount: int) -> int:
    res = []
    def backtrack(start, sum, track):
        for i in range(start, len(coins)):
            if sum + coins[i] == amount:
                res.append(len(track) + 1)
                return
            elif sum + coins[i] < amount:
                backtrack(i, sum + coins[i], track + [coins[i]])
            elif sum + coins[i] > amount:
                return
    backtrack(0, 0, [])
    if res == []:
        return -1
    else:
        return min(res)
```

[300.最长上升子序列(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/300.%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97.py)<br>
思路：子序列是可以不挨着的。我们假设dp[i]表示以第i个数字结尾的最长上升子序列长度。初始化所有dp的值为1（因为怎么样都肯定有1个最长上升子序列是一个数），每次遍历i以前的数字，如果第i个数字大于之前的某个数而且那个数的最长上升子序列长度比dp[i]的值大，则将其+1赋值给dp[i]，否则就继续遍历。最终找到最大的dp值。


```
def lengthOfLIS(self, nums: List[int]) -> int:
    dp = [1 for i in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i):
	    if nums[i] > nums[j]:
	        dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```


<br>
以上方法的时间复杂度接近O(n^2)，要想将复杂度降低到O(nlogn)，则要引入二分的思想。这种思路是LeetCode某大佬的。新建数组 tmp，用于保存最长上升子序列。对原序列进行遍历，将每位元素二分插入 tmp 中。如果 tmp 中元素都比它小，将它插到最后否则，用它覆盖掉比它大的元素中最小的那个。总之，思想就是让 tmp 中存储比较小的元素。这样，tmp 未必是真实的最长上升子序列，但长度是对的。<br>
作者：coldme-2<br>
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-e/<br>
来源：力扣（LeetCode）<br>
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。<br>

```
def lengthOfLIS(self, nums: List[int]) -> int:
   tmp = [nums[0]]
   for i in nums[1:]:
      if i > tmp[-1]:
	tmp.append(i)
    else:
	left, right = 0, len(tmp) - 1
	while (left < right):
	    mid = left + (right - left >> 1)
	    if i > tmp[mid]:
		left = mid + 1
	    elif i<tmp[mid]:
		right = mid
	    else:
		left=mid
		break
	tmp[left]=i
    return len(tmp)
```


[72.编辑距离(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/72.%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.py)<br>
思路：这种涉及到两个字符串的动态规划法都应该画个数组图。
```
   无 r o s
无 0  1 2 3
h  1  1 2 3
o  2  2 1 2
r  3  2 2 2
s  4  3 3 2
e  5  4 4 3
```

<br>
由这个图所示，很显然当末尾两个字符相等的时候，比如ho和ro，他的最短编辑次数应该为对角线，相当于h->r的次数。如果两个字符不相等，比如hor->ro。要么可以先把hor->r，也就是2步，再+1步到ro，这里为3步。要么可以把hor变成ho这里为1步，然后再从ho变为ro，这里需要1步，总共2步。要么可以想hor的ho部分变成r需要2步，然后r部分直接变成o得到ro，这里又需要1步，总共为3步。然后这三种情况中取最少的步数，也就是两步，所以可得hor->ro的步数为min(hor->ho步数+1，or->r步数+1,hor->r步数+1)=2。

```
def minDistance(self, word1: str, word2: str) -> int:
    len_word1 = len(word1)
    len_word2 = len(word2)
    dp = [[0 for i in range(len_word2 + 1)] for j in range(len_word1 + 1)]
    for i in range(len_word1+1):
        dp[i][0] = i
    for i in range(len_word2+1):
        dp[0][i] = i
    for row in range(1, len_word1 + 1):
        for col in range(1, len_word2 + 1):
	    if word1[row - 1] == word2[col - 1]:
	        dp[row][col] = dp[row - 1][col - 1]
	    else:
	        dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
    return dp[len_word1][len_word2]
```

[1143.最长公共子序列(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/1143.%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.py)<br>
思路：这种涉及到两个字符串的动态规划法都应该画个数组图。
```
   无 a c e
无 0  0 0 0
a  0  1 1 1
b  0  1 1 1
c  0  1 2 2
d  0  1 2 2
e  0  1 2 3
```

<br>
设dp[i][j]表示在text1[:i]和text2[:j]的情况下的最长公共子序列长度，那么很显然，当text1[i]=text2[j]的时候，dp[i][j]=dp[i-1][j-1]+1。如果不相等，则应该是在dp[i-1][j]和dp[i][j-1]中取最大者。
<br>

```python
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1)][len(text2)]
```

[516.最长回文子序列(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/516.%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E5%BA%8F%E5%88%97.py)<br>
思路：最长回文子序列问题，碰到相同的字符就说明可以成为最长回文子序列中的一员。dp[i][j]表示在i到j的字符串里最长的回文子序列长度。如果i和j的字符相等，那dp[i][j]长度是dp[i+1][j-1]+2，否则就相当于这两个字符不为回文字符，dp[i][j]应当是dp[i+1][j]和dp[i][j-1]中最大的一个。初始条件很显然当i=j的时候，指向的是同一个字符，此时的回文只有自己，为1。
```
def longestPalindromeSubseq(self, s: str) -> int:
    tmp = []
    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
	    if s[i] == s[j]:
	        dp[i][j] = dp[i + 1][j - 1] + 2
	        tmp.append(s[i])
	    else:
	        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][len(s) - 1]
```

[486.预测赢家(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/486.%E9%A2%84%E6%B5%8B%E8%B5%A2%E5%AE%B6.py)<br>
思路：这种问题涉及到了两组数组。我们假设dp1[i][j]为先手情况下，从数组[i]到数组[j]中，所能取得的最高分。dp2[i][j]为后手情况下，从数组[i]到数组[j]能取得的最高分。很显然，dp1[i][j]=max(nums[i]+dp2[i+1][j],nums[j]+dp2[i][j-1])。因为这次先手拿了以后，下一次拿自己就相当于是后手了，所以是+dp2的值。dp2的取值取决于dp1的选择，如果dp1选了i，则dp2[i][j]=dp1[i + 1][j],相当于在数组[i+1]到数组[j]做先手。如果dp1选择j，则 dp2[i][j]=dp1[i][j-1]，相当于在数组[i]到数组[j-1]里做先手。初始条件，很显然当i=j的时候，先手会拿走唯一的值，而后手什么也没得拿了。
```python
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp1 = [[0 for i in range(len(nums))] for j in range(len(nums))]
        dp2 = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)):
            dp1[i][i] = nums[i]
            dp2[i][i] = 0
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                left = nums[i] + dp2[i + 1][j]  # 先手的选了以后，下一次就相当于变成了后手，所以要加后手的
                right = nums[j] + dp2[i][j - 1]
                if left > right:
                    dp1[i][j] = left
                    dp2[i][j] = dp1[i + 1][j]  # 同理，这次后手的，下一次就会变成先手了
                else:
                    dp1[i][j] = right
                    dp2[i][j] = dp1[i][j - 1]
        return dp1[0][len(nums) - 1] >= dp2[0][len(nums) - 1]
```

[877.石子游戏(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/877.%E7%9F%B3%E5%AD%90%E6%B8%B8%E6%88%8F.py)<br>
思路：和[486.预测赢家]题目基本上一样，只不过多了不会平局的条件，但是这种动态规划法没有区别。
```
    def stoneGame(self, nums: List[int]) -> bool:
        dp = [[[0 for i in range(len(nums))] for j in range(len(nums))] for k in range(2)]
        for i in range(len(nums)):
            dp[0][i][i] = nums[i]
            dp[1][i][i] = 0
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                left = nums[i] + dp[1][i + 1][j]
                right = nums[j] + dp[1][i][j - 1]
                if left > right:
                    dp[0][i][j] = left
                    dp[1][i][j] = dp[0][i + 1][j] # 后手那个在这次先手选了以后就会变成先手了
                else:
                    dp[0][i][j] = right
                    dp[1][i][j] = dp[0][i][j - 1]
        return dp[0][0][len(nums)-1] > dp[1][0][len(nums)-1]
```

[121,122,123,188买卖股票的最佳时机全家桶(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/188.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIV.py)<br>、
思路：理解题意，状态无非是：天数、可交易的次数、当前已经买了还是没有买，然后要求最大的收益，不妨设dp[i][k][p]为第i天下交易了k次然后目前持有股票(p=1)或者不持有股票(p=0)的最大收益。每天可以进行的选择为[买入、卖出、不作为]，而且这些操作都被交易次数和是否持有股票所限制的。接下来看状态转移递推式：<br>
```
dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k-1][0]-当天的股票价格)
(很显然第i天已经交易了k次的持有股票的状态应该由：前一天就是这样然后不作为或者前一天交易次数-1不持股票但是今天买了这两个转移而来)
dp[i][k][0]=max(dp[i-1][k][0],dp[i-1][k][1]+当天的股票价格)
(很显然第i天已经交易了k次的持有股票的状态应该由：前一天就是这样然后不作为或者前一天持股票但是今天卖了这两个转移而来)
```

初始条件：一开始第0天，是不可能持有股票的，所以dp[0][k][1]应该设置为负无穷，这里我们只要用第一天的负价格代替就可以了。而一开始其他情况未持有的收益应该都为0。

```
def maxProfit(self, k: int, prices: List[int]) -> int:
    if len(prices)==0:
        return 0
    dp=[[[0]*2 for j in range(k+1)] for i in range(len(prices)+1)]
    for i in range(k+1):
        dp[0][i][1]=-prices[0]
    for i in range(1,len(prices)+1):
        dp[i][0][0]=dp[i-1][0][0]
        for j in range(1,k+1):
            dp[i][j][1]=max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i-1])
            dp[i][j][0]=max(dp[i-1][j][0],dp[i-1][j][1]+prices[i-1])
    return dp[len(prices)][k][0]
```

[198.打家劫舍(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/198.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D.py)<br>
思路：题目通俗来说就是不能抢相邻的。状态就是房子，选择就是抢或者不抢，目的是使抢的钱最多。那么dp[i]为第i家房子为止，最多能抢到多少。那么很显然dp[i]=max(dp[i-1],dp[i-2]+当前房子的钱),也就是要么这家房子我抢，那值应该就是我i-2个房子的最大收益加上当前房子的钱，要么不抢，那就是还保持了i-1房子的最大收益。状态转移只可能从这两个地方来。然后初始条件：很显然dp[0]=0没有房子自然收益为0，dp[1]=第一家的钱，只有一家，就只能抢他。
```
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max((dp[i - 2] + nums[i - 1]), dp[i - 1])
            # dp[i]=max(dp[i-2]的基础上抢了第i家，dp[i-1]不抢第i家)
        return dp[len(nums)]
#上述过程有很多无用空间，可以变成如下所示
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = 0
        dp1 = 0
        dp2 = nums[0]
        for i in range(1, len(nums)):
            dp = max(dp2, (dp1 + nums[i]))
            dp1 = dp2
            dp2 = dp
        return dp
```

[213.打家劫舍II(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/python/213.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DII.py)<br>
思路：和[198.打家劫舍]思路类似，只是前后围成了一个圈。那么只需要分两种情况讨论就好了，第一种是抢第一个房子，那么最后一个房子就不能抢了，去掉最后一个房子，接下来和[198.打家劫舍]一样了。第二种是不抢第一个房子，那么把第一个房子去掉，接下来又和[198.打家劫舍]一样了。
```
    def rob2(self, nums): #44ms,13.5mb
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = 0
        dp1 = 0
        dp2 = nums[1]
        for i in range(2, len(nums)):
            dp = max(dp2, (dp1 + nums[i]))
            dp1 = dp2
            dp2 = dp
        f = 0
        f1 = 0
        f2 = nums[0]
        for i in range(1, len(nums)-1):
            f = max(f2, (f1 + nums[i]))
            f1 = f2
            f2 = f
        return max(dp, f)
```

## 回溯法
解题模板：<br>
```
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```
<br>

[78.子集(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/78%E5%AD%90%E9%9B%86.py)<br>
思路：回溯法关键要确定选择列表和路径以及结束条件，但是因为子集是全部子集都要，所以没有结束条件，结束条件就是遍历完。选择列表则是上一层选择路径之后的数，也就是for i in range(start,len(数组长度)):，从上一层传递过来的start到最后。做出选择就是将当前选择的元素加入路径tmp.append(nums[i]) ，撤销选择为 tmp.pop(-1) 

```
def backtrack(start,tmp):
    result.append(tmp) # 将结果存入结果列表
    for i in range(start,len(数组长度)):
        tmp.append(nums[i]) # 添加当前路径的元素
        backtrack(i+1,tmp) # 递归下一个元素
        tmp.pop(-1) # 回溯回去的时候要撤销掉这一层的选择
    
```
[90.子集II(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/90%E5%AD%90%E9%9B%86II.py)<br>
思路：和78.子集思路一致，只不过包含了重复数字，排序好后只需要在循环中加一条剪枝条件即可。
```
def trackback(start,track):
    result.append(track)
    for i in range(start,len(nums)):
        if (i>start) and (tmp[i]==tmp[i-1]):#如果当前这条分支的数字和前一条相同，则直接跳过这条分支
            continue
        trackback(i+1,track+[tmp[i]])
```

[39.组合总数(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/39%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C.py)<br>
思路：回溯法关键要确定选择列表和路径以及结束条件，很显然一个递归的结束条件就是sum==target。选择列表是数组中的每个。for i in range(start,len(数组)),做出选择就是当sum+当前选的数小于target的时候，将track+[nums[i]]作为新的路径，sum+nums[i]作为新的目前和值，进入下一层的递归，值得注意的是，为了实现数组内每个数字可以重复无限次使用，传入下一层递归的start依然为i。
```
def trackback(start, sum, track):
    for i in range(start, len(nums)):
        if sum + nums[i] == target:  # 满足则加入答案
            result.append(track + [nums[i]])
            return
        if sum + nums[i] < target:  # 满足小于就继续递归
            trackback(i, sum + nums[i], track + [nums[i]])  # start=i,表示数字可以重复使用，这样一来就可以原地把所需要的自己都取掉
        if sum + nums[i] > target:  # 满足大于则直接剪枝
            return
```

[40.组合总数II(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/40%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.py)<br>
思路：和39.组合总数思路一致，但是在循环中加一条剪枝条件，然后由于数字无法无限次重复使用，传入下一层递归的start应该+1。
```
def trackback(start, sum, track):
    for i in range(start, len(nums)):
        if (i>start) and (nums[i]==nums[i-1]): # 如果一条分支和前面的分支数字相同，则将这条分支剪掉
            continue
        if sum + nums[i] == target:  # 满足则加入答案
            result.append(track + [nums[i]])
            return
        if sum + nums[i] < target:  # 满足小于就继续递归
            trackback(i+1, sum + nums[i], track + [nums[i]])  # start=i,表示数字可以重复使用，这样一来就可以原地把所需要的自己都取掉
        if sum + nums[i] > target:  # 满足大于则直接剪枝
            return
```
[216.组合总数III(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/216.%E7%BB%84%E5%90%88%E6%80%BB%E6%95%B0III.py)
思路：和39.组合总数与40.组合总数II类似，只不过nums变成了[1,2,3,4,5,6,7,8,9]，结束条件变成了sum + nums[i] == n且cur_num + 1 == k。
```
def trackback(sum, track, start, cur_num): # sum为目前的累加和，track为目前已经选择的数字，start表示选择列表该从哪个位置开始选，cur_sum表示当前已经选了几个数字
    for i in range(start, 9):
        if sum + nums[i] == n:
            if cur_num + 1 == k:
                result.append(track + [nums[i]])
            else:
                return
        if sum + nums[i] > n:
            return
        if sum + nums[i] < n:
            trackback(sum + nums[i], track + [nums[i]], i + 1, cur_num + 1)

```

[46.全排列(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/46%E5%85%A8%E6%8E%92%E5%88%97.py)<br>
思路：回溯法关键要确定选择列表和路径以及结束条件，很显然一个递归的结束条件就是len(路径)==len(数组)。选择列表是数组中除了前面选过的数之外的每个数，for i in range(0,len(数组)),利用一个check数组存储起来哪些数有没有被选择。
```
def backtrack(self, sol, check):
    if len(sol) == len(nums):
        self.res.append(sol)
        return
    for i in range(len(nums)):
        if check[i] == 1:
            continue
        check[i] = 1
        self.backtrack(sol + [nums[i]], check)
        check[i] = 0
```

[47.全排列II(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/47%E5%85%A8%E6%8E%92%E5%88%97II.py)<br>
思路：和46.全排列一致，只不过要将重复的分支剪掉，所以要加一句if (i > 0) and (used[i - 1] == 1) and (nums[i] == nums[i - 1])来判断是否是重复的数字。
```
def trackback(track, used):
    if len(track) == len(nums):
        result.append(track)
        return
    for i in range(len(nums)):
        if (i > 0) and (used[i - 1] == 1) and (nums[i] == nums[i - 1]):
            continue
        if used[i] == 0:
            used[i] = 1
            trackback(track + [nums[i]], used)
            used[i] = 0
```

[51.N皇后(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/51N%E7%9A%87%E5%90%8E.py)<br>
思路：回溯法关键要确定选择列表和路径以及结束条件，很显然一个递归的结束条件就是我已经放完了合法的最后一行的皇后位置。即if row == n:，选择列表是n列的位置，剪枝是判断皇后的位置是否合法，若不合法的分支则剪掉。值得注意的是，因为递归完就有撤销选择，所以不用担心同一行会出现多个皇后。剪枝只需要判断斜线和列就行了。
```
def trackback(row, cheer): # row 为棋盘的行，cheer为棋盘
    if row == n: # 一个递归的结束条件
        result.append([''.join(s) for s in cheer])
        return
    for col in range(n):
        if not isValid(row, col, cheer): # 若不合法就剪枝掉
            continue
        cheer[row][col] = 'Q'
        trackback(row + 1, cheer) # 下一层递归
        cheer[row][col] = '.'

def isValid(row, col, cheer):
    tp_row = row - 1
    tp_col = col - 1
    while (tp_col >= 0 and tp_row >= 0):  # 正对角线是否有皇后
        if cheer[tp_row][tp_col] == 'Q':
            return False
        tp_row -= 1
        tp_col -= 1
    tp_row = row - 1
    tp_col = col + 1
    while (tp_row >= 0 and tp_col < len(cheer)): #逆对角线是否有皇后
        if cheer[tp_row][tp_col] == 'Q':
            return False
        tp_row -= 1
        tp_col += 1
    for i in range(0, row): #同一列中是否有皇后
        if cheer[i][col] == 'Q':
            return False
    return True
```
[52.N皇后II(python版本)](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/52N%E7%9A%87%E5%90%8EII.py)<br>
思路：和51.N皇后思路一样，只不过不需要存储下皇后所在位置，只需要计数就可以了。
```
def trackback(row, cheer):
    if row == n:
        self.result += 1
        return
    for i in range(n):
        if not isValid(row, i, cheer):
            continue
        cheer[row][i] = 'Q'
        trackback(row + 1, cheer)
        cheer[row][i] = '.'

def isValid(row, col, cheer):
    tp_row = row - 1
    tp_col = col - 1
    while (tp_row >= 0 and tp_col >= 0): # 正对角线是否有皇后
        if cheer[tp_row][tp_col] == 'Q':
            return False
        tp_row -= 1
        tp_col -= 1
    tp_row = row - 1
    tp_col = col + 1
    while (tp_row >= 0 and tp_col < n): #逆对角线是否有皇后
        if cheer[tp_row][tp_col] == 'Q':
            return False
        tp_row -= 1
        tp_col += 1
    for i in range(row): #同一列中是否有皇后
        if cheer[i][col] == 'Q':
            return False
    return True
```

[980.不同路径III](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/980.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84III.py)<br>
思路：回溯法模拟机器人走过的所有路径，关键要确定选择列表和路径以及结束条件，很显然结束条件就是我的步数走完了所有可走的格子并且到了终点，即i == end[0] and j == end[1] and cur_step == step+1。选择列表为往上下左右走，剪枝则很明显是减去走到了非法路径和障碍物的路径和已经走过的路径。
```
def trackback(i, j, grid, cur_step): # i为当前到了的行，j为当前到了的列，cur_step为当前走的步数，grid为迷宫数组
    if i == end[0] and j == end[1] and cur_step == step+1: #step为grid中除了终点起点的可以走的格子数
        self.res += 1
        return
    grid[i][j] = -1 #先把i行j列标记为走过了
    if is_valid(i - 1, j, grid): #上
        trackback(i - 1, j, grid, cur_step + 1)
    if is_valid(i, j - 1, grid): #右
        trackback(i, j - 1, grid, cur_step + 1)
    if is_valid(i + 1, j, grid): #下
        trackback(i + 1, j, grid, cur_step + 1)
    if is_valid(i, j + 1, grid): #左
        trackback(i, j + 1, grid, cur_step + 1)
    grid[i][j] = 0 #撤销选择

def is_valid(i, j, grid): #判断是否要剪枝
    if i >= 0 and j >= 0 and i < row and j < col and grid[i][j] != -1:
        return True
    else:
        return False
```

[842.将数组拆分成斐波那契序列](https://github.com/IPostYellow/Leecode/blob/master/%E5%9B%9E%E6%BA%AF/python/842.%E5%B0%86%E6%95%B0%E7%BB%84%E6%8B%86%E5%88%86%E6%88%90%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E5%BA%8F%E5%88%97.py)<br>
思路：首先理解题目，题目的意思是给定一串字符串数字比如"123456789",要将其拆分成["123","456","789"]这种大于等于三个元素，并且后面的元素是由前面的两个元素的和组成的列表。那么可以使用回溯法不断选取数字。选择列表即整个字符串里，index后面的部分。值得注意的是还得判断字符"0"只能单独作0使用。
```python
        def trackback(index):
            if index == len(S): #遍历完整个字符串了，看看答案的列表长度是否大于2，如果是则说明找到了这个答案，否则就没有找到
                return len(res) > 2
            s = 0
            for i in range(index, len(S)):
                s = s * 10 + int(S[i]) #将字符转化成数字，存储当前选了的字符数字的值
                if S[index] == "0" and i > index: #一定要先判断前面为0的，判断完如果出现01这种情况直接剪枝
                    break
                elif s > 2 ** 31 - 1: #题目给的范围
                    break
                elif (len(res) > 2) and (res[-1] + res[-2] < s): #当前的字符的值都已经超过了res数组的后两位，则不可能使得res[-1]+res[-2]==s了，直接剪枝
                    break
                elif (len(res) < 2) or (res[-1] + res[-2] == s): #符合条件的合法部分
                    res.append(s) #选择当前s
                    if trackback(i + 1): # 目前为止是到i的字符合法被装进了res里，递归判断i+1到len(S)的符不符合条件了
                        return True
                    res.pop() # 撤销选择
            return False
```
