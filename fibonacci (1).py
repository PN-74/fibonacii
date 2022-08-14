#!/usr/bin/env python
# coding: utf-8

# # The Fibonacci Sequence is the series of numbers :
# 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# 
# Every next number is found by adding up the two numbers before it.
# 
# Expected Output : 1 1 2 3 5 8 13 21 34

# In[2]:


#Python program to generate Fibonacci series until 'n' value
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b


# In[ ]:




