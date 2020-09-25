class Stack:
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


class Stack_with_min:
    def __init__(self):
        self.stackdata = Stack()
        self.stackmin = Stack()

    def is_empty(self):
        return self.stackdata.is_empty()

    def push(self, item):
        self.stackdata.push(item)
        if self.stackmin.is_empty():
            self.stackmin.push(item)
        if self.stackmin.top() >= item:
            self.stackmin.push(item)

    def pop(self):
        if self.stackdata.top() == self.stackmin.top():
            self.stackmin.pop()
            return self.stackdata.pop()
        else:
            return self.stackdata.pop()

    def top(self):
        return self.stackdata.top()

    def get_min(self):
        return self.stackmin.top()


