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
按分类查看：[滑动窗口](#滑动窗口)、[二分搜索](#二分搜索)、[回溯法](#回溯法)<br>

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

[33.旋转排序数组](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/33%E6%90%9C%E7%B4%A2%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84.py)<br>
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

[81.搜索旋转排序数组II](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/81%E6%90%9C%E7%B4%A2%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84II.py)<br>
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

[34.在排序数组中查找元素的第一个最后一个位置](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/34%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E6%9F%A5%E6%89%BE%E5%85%83%E7%B4%A0%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%92%8C%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E4%BD%8D%E7%BD%AE.py)<br>
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

[153.寻找旋转排序数组中的最小值](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/153%E5%AF%BB%E6%89%BE%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9C%80%E5%B0%8F%E5%80%BC.py)<br>
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

[154.寻找旋转排序数组中的最小值II](https://github.com/IPostYellow/Leecode/blob/master/%E4%BA%8C%E5%88%86%E6%90%9C%E7%B4%A2/python/154%E5%AF%BB%E6%89%BE%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9C%80%E5%B0%8F%E5%80%BCII.py)<br>
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

852.山脉数组的峰顶索引
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
