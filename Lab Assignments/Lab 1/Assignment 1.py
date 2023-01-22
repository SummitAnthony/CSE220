#!/usr/bin/env python
# coding: utf-8

# 1. Shift Left k Cells
# 
# Consider an array named source. Write a method/function named shiftLeft( source, k)
# that shifts all the elements of the source array to the left by 'k' positions. You must
# execute the method by passing an array and number of cells to be shifted. After calling
# the method, print the array to show whether the elements have been shifted properly.
# Example:
# source=[10,20,30,40,50,60]
# shiftLeft(source,3)
# After calling shiftLeft(source,3), printing the array should give the output as:
# [ 40, 50, 60, 0, 0, 0 ]

# In[2]:


def shiftLeft(source, k):
    
    
    
    for count in range(k):

        for i in range(1, len(source)):
            source[i-1] = source[i]
            
        source[len(source)-1] = 0
        
    return source
        
    
    
    
    
source=[10,20,30,40,50,60]
shiftLeft(source, 3)


# 2. Rotate Left k cells
# Consider an array named source. Write a method/function named rotateLeft( source, k)
# that rotates all the elements of the source array to the left by 'k' positions. You must
# execute the method by passing an array and number of cells to be shifted. After calling
# the method, print the array to show whether the elements have been shifted properly.
# Example:
# source=[10,20,30,40,50,60]
# rotateLeft(source,3)
# After calling rotateLeft(source,3), printing the array should give the output as:
# [ 40, 50, 60, 10, 20, 30]
# 

# In[10]:


def shiftLeft(source, k):
    
    
    
    for count in range(k):
        x = source[0]
        for i in range(1, len(source)):
            source[i-1] = source[i]
            
        source[len(source)-1] = x
        
    return source
    
    
source=[10,20,30,40,50,60] 
shiftLeft(source, 3)


# 3. Shift Right k Cells
# Consider an array named source. Write a method/function named shifRight( source, k)
# that shifts all the elements of the source array to the right by 'k' positions. You must
# execute the method by passing an array and number of cells to be shifted. After calling
# the method, print the array to show whether the elements have been shifted properly.
# Example:
# source=[10,20,30,40,50,60]
# shiftRight(source,3)
# After calling shiftRight(source,3), printing the array should give the output as:
# [ 0,0,0,10,20,30 ]

# In[1]:


def shiftRight(a, k):
    
    for count in range(k):

        for i in range(len(source)-2, -1, -1):
            source[i+1] = source[i]
            
        source[0] = 0
        
    return source

source=[10,20,30,40,50,60]

shiftRight(source, 3)


# 4. Rotate Right k cells
# Consider an array named source. Write a method/function named rotateRight( source,
# k) that rotates all the elements of the source array to the right by 'k' positions. You must
# execute the method by passing an array and number of cells to be shifted. After calling
# the method, print the array to show whether the elements have been shifted properly.
# Example:
# source=[10,20,30,40,50,60]
# rotateRight(source,3)
# After calling rotateRight(source,3), printing the array should give the output as:
# [ 40, 50, 60, 10, 20, 30]

# In[26]:


def RotateRight(a, k):
    
    for count in range(k):
        x = source[-1]
        for i in range(len(source)-2, -1, -1):
            source[i+1] = source[i]
            
        source[0] = x
        
    return source

source=[10,20,30,40,50,60]

RotateRight(source, 3)


# 5. Remove an element from an array
# Consider an array named source. Write a method/function named remove( source,
# size, idx) that removes the element in index idx of the source array. You must execute
# the method by passing an array, its size and the idx( that is the index of the element to
# be removed). After calling the method, print the array to show whether the element of
# that particular index has been removed properly.
# Example:
# source=[10,20,30,40,50,0,0]
# remove(source,5,2)
# After calling remove(source,5,2) , printing the array should give the output as:
# [ 10,20,40,50,0,0,0]

# In[29]:


def remove(source, size, idx):
    if idx < 0 or idx > size:
        print("Invalid Index")
        return

    for i in range(size):
        if i >= idx and i <= size - 1:
            source[i] = source[i + 1]

    source[size - 1] = 0

    return source

source = [10,20,30,40,50,0,0]
remove(source,5,2)



# 6. Remove all occurrences of a particular element from an array
# Consider an array named source. Write a method/function named removeAll( source,
# size, element) that removes all the occurrences of the given element in the source
# array. You must execute the method by passing an array, its size and the element to be
# removed. After calling the method, print the array to show whether all the occurrences
# of the element have been removed properly.
# Example:
# source=[10,2,30,2,50,2,2,0,0]
# removeAll(source,7,2)
# After calling removeAll(source,7,2), all the occurrences of 2 must be removed. Printing
# the array afterwards should give the output as:
# [ 10,30,50,0,0,0,0,0,0]

# In[8]:


def removeall(source, size, element):
    stack = []
    
    for i in range(len(source)):
        if source[i] != element:
            stack.append(source[i])
    return stack + [0]*(len(source)-len(stack))


source=[10,2,30,2,50,2,2,0,0]
removeall(source,7,2)


# 7. Splitting an Array
# Suppose the elements of an array A containing positive integers, denote the weights in
# kilograms. And we have a beam balance. We want to put the weights on both pans of
# the balance in such a way that for some index 0 < i < A.length - 1, all values starting
# from A[0], A[1], upto A[ i - 1], should be on the left pan. And all values starting from A[ i ]
# upto A[ A.length - 1] should be on the right pan and the left and right pan should be
# balanced. If such an i exists, return true . Else, return false.
# Input: [1, 1, 1, 2, 1] Output : true
# Explanation: (summation of [1, 1, 1] = summation of [2,1])
# Input: [2, 1, 1, 2, 1] Output: false
# Input: [10, 3, 1, 2, 10] Output: true
# Explanation: (summation of [10, 3] = summation of [1,2,10]))

# In[4]:


def splitarray(source) :
    
    n = len(source)
    leftSum = 0
    

    for i in range(n):
       

        leftSum += source[i] 
    

        rightSum = 0 
        for j in range(i+1, n) :
            rightSum += source[j] 
    

        if (leftSum == rightSum) :
            return True
       
    

    return False
   


source =  [1, 1, 1, 2, 1]
splitarray(source)


# 8. Array series
# Write a method that takes an integer value n as a parameter. Inside the method, you
# should create an array of length n squared (n*n) and fill the array with the following
# pattern. Return the array at the end and print it.
# If,
# n=2: { 0,1, 2,1 } (spaces have been added to show two distinct groups).
# n=3 : { 0, 0, 1, 0, 2, 1, 3, 2, 1 } ((spaces have been added to show three distinct
# groups).
# n=4 : {0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1} (spaces have been added to show
# four distinct groups).
# 

# In[5]:


def arrayseries(n):
    stack = [0] * n**2
    
    x = 1
    while x <= n:
        y = 1
        while y <= x: 
            stack[(x*n)-y] = y

            y += 1
        x += 1
    return stack


n = 2
arrayseries(n)


# 9. Max Bunch Count
# A "bunch" in an array is a consecutive chain of two or more adjacent elements of the
# same value. Write a method that returns the number of elements in the largest bunch
# found in the given array.
# Input: [1, 2, 2, 3, 4, 4, 4] Output: 3
# Explanation: There are two bunches here {2,2} and {4,4,4}. The largest bunch is {4,4,4}
# containing 3 elements so 3 is returned.
# Input: [1,1,2, 2, 1, 1,1,1] Output:4
# Explanation: There are three bunches here {1,1} and {2,2} and {1,1,1,1}. The largest
# bunch is {1,1,1,1} containing 4 elements so 4 is returned.

# In[41]:


def Max_Bunch_Count(source):
    sum_list = []
    first = source[0]
    c = 0
    for values in source:
        if values == first:
            c += 1

        else:
            first = values
            c = 1
        sum_list.append(c)
    
    max_val = sum_list[0]
    for i in sum_list:
        if i > max_val:
            max_val = i
            
    return max_val


source = [1, 2, 2, 3, 4, 4, 4]
Max_Bunch_Count(source)


# 10.Repetition
# 
# Write a method that takes in an array as a parameter and counts the repetition of each
# element. That is, if an element has appeared in the array more than once, then its
# ‘repetition’ is its number of occurrences. The method returns true if there are at least
# two elements with the same number of ‘repetition’. Otherwise, return false.
# Input: {4,5,6,6,4,3,6,4} Output: True
# Explanation: Two numbers repeat in this array: 4 and 6. 4 has a repetition of 3, 6 has a
# repetition of 3. Since two numbers have the same repetition output is True.
# Input: {3,4,6,3,4,7,4,6,8,6,6} Output: False

# In[1]:


def repetition(lst):
    
    stack = []
    checked = []
    for i in lst:
        if i not in checked:
            count = 0
            for ele in lst:
                if (ele == i):
                    count +=1
            if count > 1:
                stack.append(count)
            checked.append(i)
 
    first = stack[0];
     
    for i in range(1, len(stack)):
        if (stack[i] != first):
            return False;
           
    return True;

 

source = [3,4,6,3,4,7,4,6,8,6,6]
repetition(source)


# In[ ]:





# In[ ]:




