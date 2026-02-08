#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
arr = np.array([[-1, 2, 0, 4], [4, -0.5, 6, 0], [2.6, 0, 7, 8], [3, -7, 4, 2.0]])
print("Original array:\n", arr)


# In[20]:


#returns every other rows
print("\nEvery other rows: \n", arr[0:3:2])


# In[21]:


#Return every other element from the entire array
arr1=np.array([1,2,3,4,5,6,7])
print("\nOriginal array:\n",arr)


# In[22]:


print("Returns every oyher elements in the array:arr[::2]:\n",arr[::2])


# In[25]:


# Slicing array
temp= arr1[:2,:3]
print ("nArray with first 2 rows and 3 columns:n", temp)


# In[1]:


#boolean array indexing 
cond=arr>2
#cond is a boolean array
temp=arr[cond]
print("\nElements greater than 2:\n",temp)


# In[2]:


import numpy as np
arr = np.array([[-1, 2, 0, 4], [4, -0.5, 6, 0], [2.6, 0, 7, 8], [3, -7, 4, 2.0]])


# In[3]:


#boolean array indexing 
cond=arr>2
#cond is a boolean array
temp=arr[cond]
print("\nElements greater than 2:\n",temp)


# In[6]:


arr = np.hstack((arr1, arr2))
print("\nHorizondal joining:\n",arr)


# In[10]:


arr1= np.array([1, 2, 3])
arr2=np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print("\nOriginal arrays:\n",arr1,arr2)
print("\nJoined array:\n",arr)


# In[11]:


#Horizondal join
arr = np.hstack((arr1, arr2))
print("\nHorizondal joining:\n",arr)


# In[12]:


#vertical join
arr=np.vstack((arr1,arr2))
print("\nVertical joining:\n",arr)


# In[13]:


#Depth join
arr=np.dstack((arr1,arr2))
print("\nDepth joining:\n",arr)


# In[16]:


#Splitting Array
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print("\nOriginal Array:\n",arr)
print("\nSplitted array:\n",newarr)
#Displaying splitted array in another form
print("\nSplitted array in another form:\n")
print(newarr[0])
print(newarr[1])
print(newarr[2])


# In[ ]:




