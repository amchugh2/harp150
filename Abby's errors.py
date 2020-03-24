#!/usr/bin/env python
# coding: utf-8

# In[1]:


# TypeError
x = 2
y = "hello"
print(x + y)


# In[2]:


# KeyError
error_dict = {"hello": 2, "goodbye": 3, "errors": 34}
print(error_dict["yo"])


# In[4]:


# IndexError
arr = [1,2,3]
for i in range(0, 10):
    if arr[i] == 5:
        print("found")


# In[5]:


# ValueError
int("hello")


# In[2]:


# Example of exception handling
x = 40
y = "hello"
try:
    print(x+y)
except TypeError:
    print("I got a Type Error")


# In[3]:


# Example of exception handling with try/catch/finally
x = 40
y = "hello"
try:
    print(x+y)
except TypeError:
    print("I got a Type Error")
finally:
    print("This will print no matter what")


# In[5]:


# Example of exception handling with try/catch/finally
x = 40
y = 20
try:
    print(x+y)
except TypeError:
    print("I got a Type Error")
finally:
    print("This will print no matter what")


# In[1]:


# Using Pixiedust example
import pixiedust
import random
%%pixiedust_debugger
def find_max(values):
    max = 0
    for val in values:
        if val > max:
            max = val
    return max
find_max(random.sample(range(100),10))


# Common Jupyter Notebook Errors

# for i in range(0,10):
#     print("hello")

# In[1]:


x = 20
y = "hello"


# In[2]:


z = x + y
print(z)


# In[3]:


import random


# In[5]:


print(random.random())


# In[ ]:




