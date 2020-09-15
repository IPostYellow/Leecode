### 记录Leetcode刷的题目
Python版本、Java版本（尚未完成）

## 滑动窗口
解题模板：<br>
windowSize=看求最大还是最小，根据不同的题目设置个初始值<br>
left,right=0<br>
while (right<len(待滑动的列表/字符串)):<br> 
(&nbsp;)(&nbsp;)对当前right位置的元素进行操作<br>
&nbsp；&nbsp；while(满足了缩小窗口的条件):<br>
&nbsp；&nbsp；&nbsp；&nbsp；缩小窗口(更新left的值)<br>
&nbsp；&nbsp；扩大窗口(更新right的值)<br>
<br>
1.[209.长度最小的子数组](https://github.com/IPostYellow/Leecode/blob/master/%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3/python/209%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.py)<br>
思路：创建一个滑动窗口和窗口尺寸，right指针不断向右移，并记录下窗口内的值的总和，如果大于等于给定的值，则判断窗口大小是否比上一次的小，如果小则更新最小窗口大小，并且不断移动left指针缩小窗口，直到窗口内总和小于给定的值为止，每移动一次left指针，再判断一次窗口内总和是否大于等于给定的值而且窗口大小是否比当前最小窗口大小小，如果是则更新最小窗口大小，否则就继续。直到right指针移动过最右边为止。消耗时间44ms,消耗内存15.2MB。<br>
