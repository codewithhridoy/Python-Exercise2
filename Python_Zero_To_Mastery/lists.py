'''
Lists are mutable that means you can change Lists wherever you want.

'''
mylist = [1,2,3,4,5,6,7,8,9,10]
         #0 1 2 3 4 5 6 7 8 9
mylist2 = [20,30,100,10,90,50,60,80,70]

mylist2.sort()
mylist2.reverse()

print(mylist2)
print(mylist[1::2])

#Adding Value (Takes exactly one argument)

mylist.append(['a','b','c','d'])
mylist.extend(['e','f','g','h'])
mylist.insert(2, 'check_insert')

print(mylist)
