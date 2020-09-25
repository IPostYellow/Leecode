class Stack:  # 基础堆栈
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.__list.pop()

    def top(self):
        if self.is_empty():
            return
        else:
            return self.__list[-1]


class Stack_with_min:  # 拥有栈内最小值信息的栈，进栈容易，出栈麻烦
    def __init__(self):
        self.stackdata = Stack()
        self.stackmin = Stack()

    def is_empty(self):
        return self.stackdata.is_empty()

    def push(self, item):
        self.stackdata.push(item)
        if self.stackmin.is_empty():
            self.stackmin.push(item)
        elif self.stackmin.top() >= item:
            self.stackmin.push(item)

    def pop(self):
        if self.stackdata.is_empty():
            return
        else:
            if self.stackdata.top() == self.stackmin.top():
                self.stackmin.pop()
                return self.stackdata.pop()
            else:
                return self.stackdata.pop()

    def top(self):
        return self.stackdata.top()

    def get_min(self):
        return self.stackmin.top()

    def print_stack(self):
        stack1 = self.stackdata
        stack2 = self.stackmin
        list1 = []
        list2 = []
        while (stack1.is_empty() == False):
            list1.append(stack1.pop())
        while (stack2.is_empty() == False):
            list2.append(stack2.pop())
        print('stack_data:', list1)
        print('stack_min:', list2)


class Stack_with_min2:  # 拥有栈内最小值信息的栈，进栈麻烦，出栈容易
    def __init__(self):
        self.stackdata = Stack()
        self.stackmin = Stack()

    def is_empty(self):
        return self.stackdata.is_empty()

    def push(self, item):
        self.stackdata.push(item)
        if self.stackmin.is_empty():
            self.stackmin.push(item)
        elif self.stackmin.top() >= item:
            self.stackmin.push(item)
        else:
            self.stackmin.push(self.stackmin.top())

    def pop(self):
        if self.stackdata.is_empty():
            return
        else:
            self.stackmin.pop()
            return self.stackdata.pop()

    def top(self):
        return self.stackdata.top()

    def get_min(self):
        return self.stackmin.top()

    def print_stack(self):
        stack1 = self.stackdata
        stack2 = self.stackmin
        list1 = []
        list2 = []
        while (stack1.is_empty() == False):
            list1.append(stack1.pop())
        while (stack2.is_empty() == False):
            list2.append(stack2.pop())
        print('stack_data:', list1)
        print('stack_min:', list2)


# s=Stack_with_min()
# s.push(1)
# s.push(1)
# s.push(5)
# s.push(4)
# s.push(7)
# s.push(0)
# s.push(1)
# s.push(9)
# s.push(0)
# s.print_stack()

s = Stack_with_min2()
s.push(1)
s.push(1)
s.push(5)
s.push(4)
s.push(7)
s.push(0)
s.push(1)
s.push(9)
s.push(0)
s.print_stack()
