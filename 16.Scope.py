#Local
'''
Name Assigned in any way within a function (def or lambda).
Not decclared Global in that function.

'''

lambda x: x**2
x = 50
def func(x):
    print('X is = ', x)
    x = 1000
    print('Local X Changed to = ', x)

func(x)
print('Global X is = {} \n'.format(x))





#Enclosing Function Locals
'''
Name in the local scope of any and all enclosing functions (def or lambda) from inner to outer.

'''
name = 'Global name'
def greet():
    name = 'Hridoy'

    def hello():
        print('Hello ' + name)

    hello()

greet()

print('Check ' + name + '\n')



#Global
'''
Name Assigned at the top-level of a module file or decclared global in a def within the file.

'''

#Built-in
'''
Name preassigned in the built in names module:
open, range, SyntaxError,...

'''

#Here X is Global variable
x = 35
def my_Function():
    #Here x is local variable
    x = 50
    return x

print('Global variable = {}'.format(x))
print('Local variable  = {}'.format(my_Function()))



x = 50
def func():
    global x
    x = 1000

print('\nBefore function call, X is = ', x)
func()
print('After function call, X is = ', x)
