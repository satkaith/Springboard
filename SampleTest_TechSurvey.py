#!/usr/bin/env python
# coding: utf-8

# In[29]:


for fizzBuzz in range(1, 15):
    if fizzBuzz % 3 == 0 and fizzBuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzBuzz % 3 == 0 and fizzBuzz % 5 != 0:
        print("Fizz")
        continue
    elif fizzBuzz % 5 == 0 and fizzBuzz % 3 != 0:
        print("Buzz")
        continue
    elif fizzBuzz % 3 != 0 or fizzBuzz % 5 != 0:
        print("Buzz")
        continue    
    print(fizzBuzz)

