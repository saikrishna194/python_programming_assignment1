#!/usr/bin/env python
# coding: utf-8

# # 1 write hello world

# In[2]:


print("Hello Python")


# # 2 Write a Python program to do arithmetical operations addition and division.?

# In[4]:


a=23
b=45
c=a+b
print(c)


# In[7]:


c=a/b
print(c)


# # 3.Write a Python program to find the area of a triangle?

# In[14]:


a=float(input("enter first side:"))
b=float(input("enter second side:"))
c=float(input("enter third side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("the area of triangle is %0.2f"%area)


# # 4. Write a Python program to swap two variables?

# In[18]:


a=input()
b=input()
temp=a
a=b
b=temp
print("a{},b{}".format(a,b))


# # 5.Write a Python program to generate a random number?

# In[23]:


import random
n=random.random()
print(n)


# In[ ]:





# In[ ]:




