#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p


class DoublyList:
  
    def __init__(self, a):
        self.head = Node(None, None, None)
        temp = self.head
        
        for i in range(len(a)):
            new_node = Node(a[i], None, None)
            temp.next = new_node
            new_node.prev = temp
            temp = temp.next
            
        temp.next = self.head
        self.head.prev = temp
  
  # Counts the number of Nodes in the list
    def countNode(self):
        #head=self.head
        c=0
        temp=self.head.next
        while temp!=self.head:
            c+=1
            temp=temp.next
            
        return c
  
  #prints the elements in the list
    def forwardprint(self):
        head = self.head.next
        tail = self.head.next.next
        while head != tail:
            print(head.element, end=" ")
            head = head.next
            tail = tail.next.next
        print()

  # prints the elements in the list backward
    def backwardprint(self):
        temp = self.head.prev
        while temp != self.head:
            print(temp.element, end=" ")
            temp = temp.prev
        print()

  # returns the reference of the at the given index. For invalid index return None.
    def nodeAt(self, idx):
        temp = self.head.next
        c = 0
        while temp != self.head:
            if c == idx:
                return temp
            c += 1
            temp = temp.next
        return Node("Index Error", None, None)
  
  
  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
    def indexOf(self, elem):
        c = 0
        temp = self.head.next
        while temp != self.head:
            if temp.element == elem:
                return c
            c += 1
            temp = temp.next
        return -1
    
  # inserts containing the given element at the given index Check validity of index. 
    def insert(self, elem, idx):
        temp = self.head
        new_node = Node(elem, None, None)
        temp1 = self.head.next
        
        if idx == 0:
            temp.next = new_node
            new_node.next = temp1
            temp1.prev = new_node
            new_node.prev = temp
            return temp1
        
        elif idx == self.countNode():
            node1 = self.nodeAt(self.countNode())
            node1.next = new_node
            new_node.prev = node1
            return temp1
        
        else:
            first = self.nodeAt(idx-1)
            second = self.nodeAt(idx)
            first.next = new_node
            new_node.next = second
            second.prev = new_node
            new_node.prev = first
            return temp1
  


    def remove(self, idx):
        count = self.countNode()
        if idx < count:
            temp = self.nodeAt(idx)
            m = temp.next
            n = temp.prev
            n.next = m
            m.prev = n
            return str(temp.element)
        else:
            return "Invalid"



#_______________________________________________________________________________________________________________________________________________________________________________


print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

# h1.forwardprint() # This should print: 10,20,30,40. 
# h1.backwardprint() # This should print: 40,30,20,10. 
# print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.  

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,85.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.


# In[ ]:




