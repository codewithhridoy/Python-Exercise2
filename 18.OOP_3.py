#Inheritence
class Animal():
    #Initialization by __init__
    def __init__(self):
        print('Animal Created')

    def who(self):
        print('It\'s an Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):
    def __init__(self):
        print('Dog Created')

    def bark(self):
        print('Bok Bok')

#who and eat function isn't in Dog Class. We inherit it from Animal Class.
mydog = Dog()
mydog.who()
mydog.eat()
mydog.bark()

#Special Methods

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    #String Representation using __str__
    def __str__(self):
        return 'Title = {}, Author = {} and Pages = {}'.format(self.title, self.author, self.pages)

    #Length Representation
    def __len__(self):
        return self.pages

    #Delete Representation
    def __del__(self):
        print("The Book is Stock Out!!!")


b = Book('Python', 'Hridoy', 500)
print(b)
print(len(b))
del b
