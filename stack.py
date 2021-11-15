mystack = []

def push(element):
    mystack.append(element)

def pop():
    if len(mystack) > 0:
        return mystack.pop()   
    """
    ele = mystack[-1]
    del mystack[-1]
    """
    return None

push(6)
push(7)
push(9)

print(pop())
print(pop())
print(pop())

print(pop())




