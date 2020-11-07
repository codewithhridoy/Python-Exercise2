
"""
Strings are immutable that means we can't change anything
into the Strings. Doesn't suppoort item assingment.

"""
#Basic
'Hridoy'
"Ahmed"

#Indexing
myStr = 'hridoy'
print(myStr)
    #1.Print First Index = h
print(myStr[0])
    #2.Print Last Index = y
print(myStr[-1])
    #3.Print any Index = d
print(myStr[3])

#Slicing
    #1.Beginning of the slice
print(myStr[2:]) # It starts Printing from index 2 to last = idoy

    #2.The end of the slice
print(myStr[:3]) # print upto 3 = hri

    #3.The later on the step slice
print(myStr[1:3]) # Start printing from 1 upto 3 = ri
print(myStr[:]) # Print entire String
print(myStr[::2]) # Start from Beginning and Jumps 2 = hio

#Basic Methods
"""
Check 9.String_Methods.py

"""
#Print Formatting
x = "Firstname = {f} & Lastname = {l}".format(l='Ahmed', f = 'Hridoy')
print(x)
