#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Q4. Write a program to print the first non-repeated character from a string?

str1=input("enter a string")
cnt=0
x={}
for i in range(len(str1)):
    if str1[i] in x.keys():
        continue
    for j in range(i+1,len(str1),1):
        if str1[i] == str1[j]:
            cnt+=1
    x[str1[i]]=cnt
    cnt=0

for i in x:
    if x[i]==0:
        print("First Non-repeated value is ",i)
        break
    
print(x)

