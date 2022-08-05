#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Q9. Write a program to reverse a stack.

class stack:
    def __init__(self):
        self.stack = []


    def push(self,value):
        self.stack.append(value)
        print("Successfully Added ")

    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty !!")
            return
        value=self.stack.pop()
        return value

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty !!")
            return
        return self.stack[len(self.stack)-1]

    def reverse_a_stack(self):
        x=self.stack[::-1]
        return x
    
obj=stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print(f"Before Reverse {obj.stack}")
print(f"After Reverse {obj.reverse_a_stack()}")

