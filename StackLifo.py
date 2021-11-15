class StackLifo():

    def __init__(self):
        self.__mystack = []
    
    def push(self,element):
        self.__mystack.append(element)
    
    def pop(self):
        if len(self.__mystack) > 0:
            return self.__mystack.pop()
        return None

    def __private(self):
        pass

"""
stack = StackLifo()
#print(stack.mystack)
stack.push(5)
stack.push(7)
stack.push(9)

#print(stack.__dict__)
print(stack._StackLifo__mystack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.pop())

"""








