def my_Function(parameter= 'default'):
    print('Check Function with {} parameter'.format(parameter))

my_Function()


def sum(num1, num2):
    return num1 + num2
sum = sum(45, 50)
print(sum)

#Filter
myList = [1, 20, 2, 8, 40, 6, 5, 80, 4556, 150, 25]
myList.sort()
def evenNum(num):
    return num%2 == 0
evens = filter(evenNum, myList)
print(list(evens)) # without list it gives an error

#lambda Expression
myList = [1, 20, 2, 8, 40, 6, 5, 80, 4556, 150, 25]
myList.sort()
evens = filter(lambda num:num%2 == 0, myList)
print(list(evens))


#in
print('x' in ['x', 1, 5, 5] )


#Exercise 1 (1,2,3,1,3)-> True

def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

#Exercise 2 heelllloo->hello
#myString[::2] or
def StringBits(myString):
    result = ''
    for i in range(len(myString)):
        if i%2 == 0:
            result = result + myString[i]
    return result

#Exercise 3 endswith method 'hiabc', 'abc' -> true
def end_other(a,b):
    a = a.lower()
    b = b.lower()

    #return(b.endswith(a) or a.endswith(b))
    return a == b[-len(a):] or b == a[-len(b):]

#Exercise 4 Double Character: the-> tthhee
def doubleChar(myString):
    result = ''
    for char in myString:
        result += char*2
    return result

#Exercise 5 : 13,14,17,18,19 count hbe na

def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n [13,14,17,18,19]:
        return 0
    return n

#Exercise 6 :  Count even integers from a given array

def countEven(nums):
    count = 0
    for i in nums:
        if i%2 == 0:
            count += 1
        return count
