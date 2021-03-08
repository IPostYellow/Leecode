class Bi_listnode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class DIYcache:
    def __init__(self):
        self.hashmap={}
        self.head=Bi_listnode(None,None)
        self.tail=Bi_listnode(None,None)
        self.head.next=self.tail
        self.tail.prev=self.head
    def move_to_tail(self,key):
        tmp_node=self.hashmap[key]
        tmp_node.prev.next,tmp_node.next.prev=tmp_node.next,tmp_node.prev
        tmp_node.prev=self.tail.prev
        tmp_node.next=self.tail
        self.tail.prev.next=tmp_node
        self.tail.prev=tmp_node
    def first_put(self,key,val):
        new_node=Bi_listnode(key,val)
        self.hashmap[key]=new_node
        new_node.next=self.tail
        new_node.prev=self.tail.prev
        self.tail.prev.next=new_node
        self.tail.prev=new_node
    def get(self,key):
        if key in self.hashmap:
            self.move_to_tail(key)
            return self.hashmap[key].val
        else:
            return None
    def put(self,key,data):
        if key in self.hashmap:
            self.move_to_tail(key)
        else:
            filename=self.head.next.val
            self.hashmap.pop(self.head.next.key)
            self.head.next.next.prev=self.head
            self.head.next=self.head.next.next
            with open(filename,"w") as f:
                f.write(data)
            new_node=Bi_listnode(key,filename)
            self.hashmap[key]=new_node
            new_node.next=self.tail
            new_node.prev=self.tail.prev
            self.tail.prev.next=new_node
            self.tail.prev=new_node

cache=DIYcache()
cache.first_put(1,"1.csv")
cache.first_put(2,"2.csv")
def surveydetail(request):
    id=request.GET.get("id")
    filename=cache.get(id)
    if filename is not None:
        with open(filename,'r') as f :
            data=f.read(1024)
        return render(request,"home.html",{"msg":data})
    else:
        survey=models.survey.object.get(id=id)
        data=serviraztion(survey)
        cache.put(id,data)
        return render(request,"home.html",{"msg":data})

