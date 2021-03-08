class BiListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curcache = 0
        self.hashmap = {}
        self.head = BiListNode(None, None)
        self.tail = BiListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, key):  # 将节点移动到尾端
        tmp_node = self.hashmap[key]
        tmp_node.next.prev = tmp_node.prev  # 断开tmp_node的后面的箭头
        tmp_node.prev.next = tmp_node.next  # 断开tmp_node前面的箭头
        # 如此一来，tmp_node前后的node就连起来了，把tmp_node取出来了

        tmp_node.next = self.tail  # 将取出的tmp_node放到tail前面，原本tail前面node的后面
        tmp_node.prev = self.tail.prev
        self.tail.prev.next = tmp_node
        self.tail.prev = tmp_node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_to_tail(key)
            return self.hashmap[key].val
        else:
            return -1
    def first_put(self,key,value):
        new_node = BiListNode(key, value)
        self.hashmap[key] = new_node
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node
    def put(self, key: int,data) -> None:
        if key in self.hashmap:
            self.move_to_tail(key)
        else:
            filename=self.hashmap[self.head.next.key].val
            with open(filename,"w") as f:
                f.write(data)
            self.hashmap.pop(self.head.next.key)
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
            new_node = BiListNode(key,filename)
            self.hashmap[key] = new_node
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev.next = new_node
            self.tail.prev = new_node
cache=LRUCache(2)
cache.put(1,"1.csv")
cache.put(2,"2.csv")

def surveydetailview(request):
    global cache
    id=request.GET.get("id")
    filename=cache.get(id)
    if filename!=-1:
        with open(filename,"r") as f:
            msg="xxx"
            pass
        return render(request, 'home.html', {'msg': msg})
    else:
        data=model.suervy.object.filter(id=id)
        cache.put(id,data)
        return render(request,"home.html",{"msg":data})
