"""
Lists are python's form of array
Lists are mutable so we can extend it.

"""
myList = [1,2,3,4,4,45,['a','d','b', 'c']]
print("Before Assignment: ")
print(myList)

#Append added the list not value
myList.append(['New Item', 'new2', 'new3'  ])
print("After Assignment: ")
print(myList)

#But extend added value with strings not the lists
newList = ['m', 'n', 'o', 'p']
myList.extend(newList)
print(myList)

#indexing
print(myList[6][2])
print(myList[7][1])

#List Comprehension
matrix = [[1,2,3], [4,5,6], [7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)


#Pop remove the last Item and print it, we can also remove by indexing
item = myList.pop()
item2 = myList.pop(0)
print(item)
print(item2)

#reverse Lists
revList = ['a', 'b', 'c', 'd', 'e']
revList.reverse()
print(revList)

#Sort
sortList = [2,5,1,0,546,435,64,632,5,3453,100]
sortList.sort()
print(sortList)
