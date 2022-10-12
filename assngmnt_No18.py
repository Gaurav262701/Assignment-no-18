#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Answer No 1
def filter_list(l):
    string = []
    for i in l:
        if type(i) == int and i >= 0:
            string.append(i)
    return string
print(f'{filter_list([1,2,"a","b"])}')
print(f'{filter_list([1,"a","b",0,15])}')
print(f'{filter_list([1,2,"aassf","1","123",123])}')


# In[5]:


#Answer No 2
def reverse(string):
    print(f'{string} -- {string[::-1].swapcase()}')
reverse('Hello World')
reverse('ReVeRsE')
reverse('Radar')


# In[6]:


#Answer no 3
first , *middle, last = [1,2,3,4,5,6]
print(f'first--{first}')
print(f'middle--{middle}')
print(f'last--{last}')


# In[7]:


#Answewr no 4
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(f'factorial(5)--{factorial(5)}')
print(f'factorial(4)--{factorial(4)}')
print(f'factorial(3)--{factorial(3)}')
print(f'factorial(0)--{factorial(0)}')


# In[8]:


#Answer no 5
def move_to_end(list,num):
    first_end = []
    second_end = []
    for i in list:
        if i == num:
            second_end.append(i)
        else:
            first_end.append(i)
    first_end.extend(second_end)
    return first_end
print(f'move_to_end([1,3,2,4,4,1],1)--{move_to_end([1,3,2,4,4,1],1)}')
print(f'move_to_end([7,8,9,1,2,3,4],9)--{move_to_end([7,8,9,1,2,3,4],9)}')
print(f'move_to_end(["a","a","a","b"],"a")--{move_to_end(("a","a","a","b"),"a")}')


# In[ ]:




