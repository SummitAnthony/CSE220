#!/usr/bin/env python
# coding: utf-8

# ## Task 1 

# In[9]:



#Task 1b

n = int(input())
memo = {}

def fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n in memo:
        return memo[n]
    
    result = fibonnaci(n-1) + fibonnaci(n-2)
    memo[n] = result
    return result

fibonnaci(n)

# Task 1c
def printArray(arr, index=0):
    if len(arr) == index:
        return
    
    print(arr[index])
    printArray(arr, index+1)
    
    
printArray([1, 2, 3, 4, 5])


# Task 1d

def powerN(base, n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    
    memo[n] = base * powerN(base, n-1)
    return memo[n]

print(powerN(3, 1))
print(powerN(3, 2))
print(powerN(3, 3))


# ## Task 2 

# In[8]:


#2a 

def decimalToBinaryMemo(num, memo = {}):
    if num == 0:
        return 0

    if num in memo:
        return memo[num]

    memo[num] = decimalToBinaryMemo(num // 2) * 10 + (num % 2)

    return memo[num]

decimalToBinaryMemo(10)

#Task-2b

class Node:
    
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        
        
class Singlelinkedlist:
    
    def __init__(self):
        self.head = None
        
        
    def push(self, elem):
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            new_node = self.head
            
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
                
            temp.next = new_node
            
    def printList(self):
        if self.head is None:
            return
        
        else:
            temp = self.head
            while temp != None:
                print(temp.elem, "->",temp.next)
                temp = temp.next
                
                
Linkedlist = Singlelinkedlist()
Linkedlist.push(10)
Linkedlist.push(20)
Linkedlist.push(30)
Linkedlist.push(40)
Linkedlist.push(50)


def addlist(head):
    if head == None:
        return 0
    
    return head.elem + addlist(head.next)


print(addlist(Linkedlist.head))


#2c

class Node:
    
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        
        
class Singlelinkedlist2:
    
    def __init__(self):
        self.head = None
        
    def push(self, elem):
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            new_node = self.head
            
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
                
            temp.next = new_node

            
            
Linkedlist1 = Singlelinkedlist2()
Linkedlist1.push(10)
Linkedlist1.push(20)
Linkedlist1.push(30)
Linkedlist1.push(40)
Linkedlist1.push(50)


def reverse(head):
    if head == None:
        return 
    
    reverse(head.next)
    print(head.elem)
    
    
reverse(Linkedlist1.head)


# ## Task 3 

# In[5]:




def hocBuilder(height):
    if height<=0:
        return
    elif height==1:
        return 8
    else:
        return 5+hocBuilder(height-1)
    
    
x=hocBuilder(3)
print(x)


# ## Task 4 

# In[3]:


#a

def recursionPattern(num,count=1,memo={}):
    if count in memo:
        return memo[count]
    elif count==num+1:
        return
    else:
        for x in range(1,count+1):
            print(x,end='')
        print()
        memo[count]=recursionPattern(num,count+1,memo)
num=int(input('Input:'))
recursionPattern(num)

#b


def recursionReversePattern(num1,count1=1,memo={}):
    if count1==num1+1:
        return
    else:
        if count1 in memo:
            val = memo[count1]
        else:
            print(' '*(num1-count1),end='')
            for y in range(1,count1+1):
                print(y,end='')
            print()
            val = recursionReversePattern(num1,count1+1,memo)
            memo[count1] = val
    return val

num1=int(input('Input:'))
recursionReversePattern(num1)


# ## Task 5 

# In[2]:


class FinalR:
    
    def print(self, arr, index=0):
        if index < len(arr):
            profit = self.calProfit(list[index])
            print("{0}. Investment:{1}; Profit:{2}".format(index+1, arr[index], profit))
            self.print(arr, index + 1)
            
    def calProfit(self, investment):
        investment -= 25000
        if investment >= 75000:
            profit = 75000 * (4.5/100)
            investment -= 75000
        else:
            profit = investment * (4.5/100)
            investment = 0
        profit = investment * (8/100) + profit
        return profit

arr = [25000, 100000, 250000, 350000]
r = FinalR()
r.print(arr, 0)


# In[ ]:




