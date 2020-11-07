#If Else if
print("Enter First Value: ")
a = int(input())

print("Enter Second Value: ")
b = int(input())
c = a + b
if c > 10:
    print('Sum is greater than 10')
elif c < 10:
    print('Sum is less than 10')
else:
    print('Sum is equal 10')

#Loops
    #1. For Loops
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in number:
    print(num)

    #Using Range
for item in range(0,20,2):
    print(item)

    #For in List Comprehension
x= [1,2,3,4]
result = [num ** 2 for num in x]
print(result)


    #2.While Loops
i = 0
while i < 5:
    print('Num is : {}'.format(i))
    i += 1
