'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：
LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]
解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Bilistnode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Bilistnode(None, None)
        self.tail = Bilistnode(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
        tmp_node = self.hashmap[key]
        tmp_node.next.prev = tmp_node.prev
        tmp_node.prev.next = tmp_node.next

        tmp_node.prev = self.tail.prev
        tmp_node.next = self.tail
        self.tail.prev.next = tmp_node
        self.tail.prev = tmp_node

    def get(self, key: int) -> int:
        if key in self.hashmap.keys():
            self.move_node_to_tail(key)
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap.keys():
            self.hashmap[key].val = value
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next.next.prev = self.head
                self.head.next = self.head.next.next
            now_node = Bilistnode(key, value)
            self.hashmap[key] = now_node
            self.tail.prev.next = now_node
            now_node.next = self.tail
            now_node.prev = self.tail.prev
            self.tail.prev = now_node

s = LRUCache(2)
print(s.put(1, 1))
print(s.put(2, 2))
print(s.get(1))
print(s.put(3, 3))
print(s.get(2))
print(s.put(4, 4))
print(s.get(1))
print(s.get(3))
print(s.get(4))

#第二次
class BilistNode2:
    def __init__(self,key,val) -> None:
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hashmap={}
        self.head=BilistNode2(None,None)
        self.tail=BilistNode2(None,None)

        self.head.next=self.tail
        self.tail.prev=self.head

    def move_to_tail(self,key):
        tmp=self.hashmap[key]
        tmp.next.prev=tmp.prev
        tmp.prev.next=tmp.next

        self.tail.prev.next=tmp
        tmp.prev=self.tail.prev
        self.tail.prev=tmp
        tmp.next=self.tail

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_to_tail(key)
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].val=value
            self.move_to_tail(key)
        else:
            if self.capacity==len(self.hashmap):
                self.hashmap.pop(self.head.next.key)
                self.head.next.next.prev=self.head
                self.head.next=self.head.next.next
            new_node=BilistNode2(key,value)
            self.hashmap[key]=new_node
            new_node.prev=self.tail.prev
            self.tail.prev.next=new_node
            self.tail.prev=new_node
            new_node.next=self.tail