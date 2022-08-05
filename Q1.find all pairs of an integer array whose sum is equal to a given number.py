#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
int_arr = [7,8,9,2,8,5,7,6]
given_no = 15 
pair_arr = []
for i in range(len(int_arr)-1):
    for j in range(i+1,len(int_arr)):
        sum = int_arr[i]+int_arr[j]
        if sum == given_no:
            pair_arr.append([int_arr[i],int_arr[j]])
print(pair_arr)


# In[ ]:




