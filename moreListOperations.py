'''
max(list): Returns the list item with the maximum value
min(list): Returns the list item with minimum value
list.count(item): Returns a count of how many times an item occurs in a list
list.remove(item): Removes an object from a list
list.reverse(): 
'''

nums = []
for i in range(1,21):
    nums.append(i)

print("Initially :",nums,sep="\t",end="\n")

print("Max val :",max(nums),sep="\t",end="\n")
print("Min val :",min(nums),sep="\t",end="\n")

nums.append(33)
nums.append(27)
nums.append(10)
nums.append(10)
print("Some appends :",nums,sep="\t",end="\n")
print("Index of 10:",nums.index(10),sep="\t",end='\n')
print("Count of 10s :",nums.count(10),sep='\t',end='\n')
print("REmoving 10 :",end=" ")
nums.remove(10)
print(nums)
nums.reverse()
print('Numbers in reverse :',nums,sep=" ",end='\n')



