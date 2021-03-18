"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-median-from-data-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import heapq

"""
3 1 5 4
大堆  小堆
 3         此时中位数为3.0
大堆 小堆 大堆比小堆多2  大堆   小堆
 3         -----》      1      3    此时中位数为 大堆顶/2+小堆顶/2 =2.0
 1
 大堆 小堆  小堆比大堆多1  大堆    小堆     
  1    3      ------》     3      5    只要堆不相等，中位数就是大堆顶，为3.0
       5                   1
大堆   小堆   
 3      4    -------》堆相等 中位数 为 大堆顶/2+小堆顶/2
 1      5
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or -self.maxHeap[0] >= num:  # python 默认的只有最小堆，所以需要取负数来判断，取出来再加个负号让他变成最大的正数。比最大堆小的加入最大堆
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:  # 两个堆的规模要保持至多最大堆只比最小堆多1
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0]/2.0+self.minHeap[0]/2.0
        else:
            return -self.maxHeap[0]/1.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
medianOfAStream = MedianFinder()
medianOfAStream.addNum(3)
medianOfAStream.addNum(1)
print("The median is: " + str(medianOfAStream.findMedian()))
medianOfAStream.addNum(5)
print("The median is: " + str(medianOfAStream.findMedian()))
medianOfAStream.addNum(4)
print("The median is: " + str(medianOfAStream.findMedian()))
