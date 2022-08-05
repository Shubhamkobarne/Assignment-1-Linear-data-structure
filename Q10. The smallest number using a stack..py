#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Q10. Write a program to find the smallest number using a stack.

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
    
    def smallest_no(self):
        min_value=999999
        for i in range(len(self.stack)):
            if self.stack[i] < min_value:
                min_value=self.stack[i]
        return min_value
        
        

obj=stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)

print(f"Small Number Is  {obj.smallest_no()}")

