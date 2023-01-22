#!/usr/bin/env python
# coding: utf-8

# #### Selection Sort Iteratively 

# In[31]:


def selection_sort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        
    return arr



arr = [5,10,9,2,1,3]
selection_sort(arr)


# #### Selection Sort Recursively  

# In[2]:


def selection(arr, i=0, j=1, flag = True):
    size = len(arr)
    if i < size-1:
        if flag:
            j = i+1
        
        if j < size:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            selection(arr, i,j+1, False)
        else:
            selection(arr, i+1, 0, True)
            

arr = [5,10,9,2,1,3]
selection(arr)
print(arr)


# #### Singly Linked List using Bubble sort and Selection Sort

# In[3]:


class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        

        
class Singlelinkedlist:
    
    def __init__(self):
        self.head = None
        
        
    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            
            
    def printFull(self):
        temp = self.head
        
        while temp.next != None:
            print(temp.val, end=",")
            temp = temp.next
        print(temp.val)
        
        
    def bubble_sort_ex_val(self):
        end = None
        while self.head.next != end:
            temp = self.head
            while temp.next != end:
                temp1 = temp.next
                if temp.val > temp1.val:
                    temp.val, temp1.val = temp1.val, temp.val
                
                temp = temp.next
                
            end = temp
            
    def selection_sort(self):
        
        temp = self.head
        while temp:
            minn = temp
            r = temp.next
            
            while r:
                if minn.val > r.val:
                    minn = r
                r = r.next
                
            #swap 
            x = temp.val
            temp.val = minn.val
            minn.val = x
            temp = temp.next
            
            
            
            
        
s1 = Singlelinkedlist()
s1.push(50)
s1.push(20)
s1.push(40)
s1.push(10)
s1.push(30)
s1.push(70)
s1.push(60)
s1.printFull()
# s1.bubble_sort_ex_val()
# s1.printFull()
s1.selection_sort()
s1.printFull()


# #### Doubly Linked List Insertion Sort

# In[33]:


class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class Doublylinkedlist:
    def __init__(self, array):
        self.head = Node(array[0], None, None)
        tail = self.head
        for x in range(1, len(array)):
            new_node = Node(array[x], None, tail)
            tail.next = new_node
            tail = new_node

    def showList(self):
        if self.head.next is None:
            print("Empty list")
        else:
            head = self.head
            while self.head is not None:
                if head.next is None:
                    print(head.value)
                    break
                else:
                    print(head.value, end=" ")
                    head = head.next

    
    
    
    def insertion_sort(self):
        head = self.head
        if head == None:
            return
        else:
            while head is not None:
                tail = head.next
                while tail and tail.prev != None and tail.value < tail.prev.value:
                    tail.value, tail.prev.value = tail.prev.value, tail.value
                    tail = tail.prev
                head = head.next


array = [7, 6, 9, 3, 5, 99, 1]
doublylinkedlist = Doublylinkedlist(array)
doublylinkedlist.insertion_sort()
doublylinkedlist.showList()


# #### Binary Search Recursive 

# In[11]:


def rec_binary_search(array, left, right, value):
    
    if left > right:
        return -1
    
    else:
        mid_value = ((left+right)//2)
        if array[mid_value] < value:
            return rec_binary_search(array, mid_value+1,right,value)
        elif array[mid_value] > value:
            return rec_binary_search(array, left, mid_value-1,value)
        else:
            return mid_value
    
    


array = [1, 2, 3, 4, 5, 6, 7]
left = 0
right = len(array)
value = 6
print(rec_binary_search(array, left, right, value))


# #### Implement a recursive algorithm to find the n-th Fibonacci number using memoization

# In[10]:


def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-2) + fib(n-1)
    return memo[n]

fib(100)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




