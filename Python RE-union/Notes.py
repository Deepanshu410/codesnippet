#a = 1
#print('hellow world'), '' or "" doesn't matter
#print(f'f for adding format while also printing a variable {a}')
# {} is called a placeholder
#variable = a container for a value, behaves as if it is the value it contains
#a is a variable containing value 1
#strings = 'for cogers = 34 
#integers for containing characters'
#intehole numbers
#float = 0.5
# float for decimals
b = True
# boolean for True or False , they're binary

#type cast# ing is the process of converting a variable from one data type to another 
# str(), int(), float(), bool()
#print(type(a)) for finding the type, if the variable is string, integar, float, or boolean
c = 35
#to convert overwrite the variable
c = float(c)
#print(c)
#this will change c from 35 to 35.0

# input() = a function that prompts the user to enter data, returns the entered data as a string
#name = input('what is your name')
#print(name)

#arithmetic operators;
f = 0
f = f + 1 #this is same as below one
f += 1 # =+, this is called augmented assignment operator 
# plus(+), minus(-), multiply(*), division(/), exponentiation or exponent or power or times(**), modulus to find out remmainder(%), floor division(//) a divisional floor operation that divides two numbers and rounds the result down to the nearest whole integer[difference -> 7//2=3, 7/2 =3.5] 

#functions of integers 
x = 3.12 
y = -4 
z = 5
result = round(x) # this rounds this value of decimal to int, but class of variable isn't changed
result1 = abs(y) # abs = absolute value, which is the distance away form zero as a whole number
result2 = pow(4, 3, 3) # pow = power, Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
result3 = max(x, y, z) # max = maximum, returns biggest item
result3 = min(x, y, z) # min = maximum, returns smallest item

# import math
# print(math.pi) #pi = value of pie
# print(math.e) #e = exponential consant 
# print(math.sqrt(x)) # for finding out square root
# print(math.ceil(x)) # rounds up demical number up to next whole number
# print(math.floor(x)) # rounds up demical number down to previous whole number, same as round function

#statements
#age = int(input('enter your age:\t'))
#if age >= 21:
#    print("You're welcome to join the club")
#elif age<=0:
#    print('Enter a correct number')
#elif age<21:
#    print("You must be 21 to proceed")
#else:
#    print('Please enter your age correctly')


#Logical Statements = evaluate multiple conditions (or, not, and)
# or = at least one condition must be True, and = both conditions must be True, not = inverts the condition (not False, not True)


#conditional expression = a one line shortcut for the if-else statement (ternary operator), print or assign one of two values based on a condition, x if condition else y

na = True
#print("affirmative" if na else "negative")
na1 = 2
re = "Even" if na1 % 2 == 0 else "Odd"
#print(re)


# String Functions and methods 
stra = 'heyloy'
pho = '323-33-33'
conc = len(stra) #function
conc1 = stra.find('y') #method, starts counting from zero, finds position
conc2 = stra.rfind('y') # last character position
conc3 = stra.capitalize() # function, capitalizes only the first character
conc4 = stra.upper() # all of the letters uppercase
conc5 = stra.lower() # all of the letters lowercase
conc6 = stra.isdigit() # method, boolean, only returns true if all the characters in the string are digits, no space or it'll be false
conc7 = stra.isalpha() # method, boolean, only returns true if all the characters in the string are alphabets, no space or it'll be false
conc8 = pho.count("-") # method, counts number of occurances
conc9 = pho.replace("-", " ") # method, replaces all of the occurances
#print(conc9)
#print(help(str)) #for exploring other string functions and methods

# indexing == accesing elements of a sequence using [] (indexing operator), [start : end : step]
# start index is incluse, end index is excluse(doesn't include itself) 
nol = "12-34-56-78-90"
# print(nol[-5])
# print(nol[0])
# print(nol[:5])  
# print(nol[::3])
# print(nol[-5:]) # prints last 4 numbers
# print(nol[::-1]) # reverses the string 


# format specifiers = {value:flags} format a value based on what flags are inserted
# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

doe = 200000.1239
doe1 = -30000.1345
# print(f'decimal {doe:.2f}')
# print(f'adds spaces to achieve the total number of character = 11\n {doe:11}|')
# print(f'adds 0 to achieve the total number of character = 11\n  {doe:011} |end')
# print(f'aligns the value to the left and adds spaces to achieve the total number of character = 11, after the value,\n {doe:<11} ,|end')
# print(f'aligns the value to the right and adds spaces to achieve the total number of character = 11,\n {doe:>11} ,|end')
# print(f'aligns the value to the centre and adds spaces to achieve the total number of character = 11,\n  {doe:^11} ,|end')
# print(f'indicates positive value with + sign, {doe:+}\n{doe1:+} ,|end')
# print(f'space when positive and no space if minus (only when mentioned minus), {doe: }\n{doe1: },|end')
# print(f'comma separator, {doe:,}\n{doe1:,} |end')
# print(f'everythin {doe:+,.2f}\n{doe1:+,.2f}')

# while loop = execute some code while some condition remains true
# lik = input("you like? (y/n)")
# while not lik == "n":
#    print("i like, hehe")
#    lik = input("you like? (y/n)")
# print("You don't like, awoh")

# for loop = execite a block of code a fixed number of times. Can iterate over a range, string, sequence, etc.
# for x in range(1, 11, 3): #  range(start, stop[, step]) 
#     print(x)

# for y in range(1, 11): # This variable must be integer
#     if y == 3:
#         continue
#     else: 
#         print(y)
#     if y == 7:
#         break

# nested loop = a loop within another loop (outer, inner)
#   outer loop:
#       inner loop:

# for x in range(3):
#     for y in range(1, 11):
#         print(y, end=" ")
#     print()


# COLLECTION = single "variable" used to store multiple values
# list = [] ordered and changeable. Duplicates OK. Are iterable. Reversable
# set = {} unordered and immutable, but Add/Remove OK. NO Duplicates. NOt reversable
# tuple = () ordered and unchangeable. Duplicates OK. Faster. Reverable
# dictionary 

fu = ["apple", "banana", "money", "paisa", "paisa"]
# print(fu[::-1])
# len(), to find length
fu[2] = "paisa" # variable stored in list can be changed
# print("money" in fu)# with the "in" operator, we can find if a variable is in a collection
# fu.append("coconut") # to add a variable in last of a list
# fu.remove("coconut") # to remove any variable in a list
# fu.insert(0, "coconut") # to insert a variable at a given index in a list
# fu.sort() # sorts a list in alphabatic order
# fu.reverse() # reverses vairables of a list in the order assigned
# print(fu.index("paisa")) # to find index of a vairable
# fu.clear() # clears the whole listS
# print(fu.count("paisa"))

su = {"app", "bana", "coco"}
# in sets, can't use indexing or sort, can use "in" operator, clear, 
su.add("mon")
su.remove("mon")
su.pop() # will remove whatever element is first, and it will be random

# in tuple, indexing is applicable


# 2D COLLECTION
#2d list = [list1, list2, list3]
groc = [["orange", "apple", "banana"], ["pork", "meat", "chicken"], ["salt", "chilly", "turmeric"]]
# print(groc[0][0])
# for collec in groc:
#     for foo in collec:
#         print(foo, end=" ")
#     print()


# DICTIONARY = a collection of {key:value} pairs, ordered and changeable. No duplicates, keys are iterable

capitals = {"USA": "Washington D.C.",
            "India":"New Delhi"}
capitals.get("USA")
capitals.get("Japan") # Returns none
capitals.update({"Germany":"Berlin"}) #adds key and value
capitals.update({"USA":"Detroit"}) #updates key or value
capitals.pop("Germany") # removes the key and value
# capitals.popitem() # removes the latest key item
# capitals.clear() #clears all if the items
capitals.keys() #to get only keys of a dictonary
capitals.values() #to get only values of a dictonary
capitals.items() # returns objects that resembles a 2d list of tuples
# for key, value in capitals.items():
#     print(f"{key}: {value}")


# RANDOM MODULE

import random
r_1 = ["2", "3", "4", "5","6", "7", "8", "9", "10"]
r0 = ("hey", "hi", "hello")
r = random.randint(1, 6) # returns a random number
r1 = random.random() # returns a random floating point number between 0 and 1
r2 = random.choice(r0) # returns random value stored in a variable
r3 = random.shuffle(r_1) # shuffles values stored in a variable


# FUNCTION = A block of reusable code, place() after the function name to invoke it

def hbday(nam, ty):
    print(f"hey {nam}, {ty}")
# hbday("YOU", "HUMAN") # positional arguments
# hbday("ME","ALIEN" )


# RETURN = Statement used to end a function and send a result back to the caller 
def add(x,y):
    z = x + y
    return z
# print(add(1, 2))


# DEFAULT ARGUMENTS = A default value for certain parameters, default is used when that argument is omitted, make your functions more flexible, reduces # of arguments; 1. Positional, 2. Default, 3. Keyword, 4. Arbitary
# to use deafult argument, they should be after positional argument
def net_price(price, discount=0, tax=0.05):
    return price * (1 - discount) * (1 + tax)
# print(net_price(100, 0.1, 0)) # given argument would be taken even if there's a  default


# KEYWORD ARGUMENTS = An argument preceded by an identifier, helps with readability, order of arguments doesn't matter 
# end=" ", is a keyword argument
# if you were to mix positional and keyword argument, the positional should be first then keyword
def hello(greet, tit, fir, las):
    print(f"{greet}, {tit}{fir} {las}")
# hello("hey", tit="Mr.", las="J", fir="D")
# print("1", "2", "3", "4", "5", sep="_")


# ARBITARY ARGUMENTS;
# *args = allows you to pass multiple non-key arguments or arbitary positional arguments  (tuple),
# **kwargs = allows you to pass multiple keyword arguments {dictionary},
# * = unpacking operator
# to use args and kwargs together, args(positional) should be put first then kwargs(arbitary)
def dnam(*aars):
    for aar in aars:
        print(aar, end=" ")
    print()
# dnam("HEY", "wth", "are you doing here")
def adrs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
# adrs(phase="7", street="KG", district="naini")


# ITERABLES = An object/ collection that can return its elements one at a time, allowing it to be iterated over in a loop 
# for number in reversed(numbers): for iterating the values in reversed form
# iterable items: tuples(), sets{}, list[], string"", dictionary{}


# MEMBERSHIP OPERATORS = used to test whether a value or variable is found in a sequence, which include but are not limited to -> (string, list, tuple, set, or dictionary)
# 1. in, 2. not in


# LIST COMPREHENSION = A concise way to create lists in Python. Compact and easier to read than traditional loops 
# format = [expression for value in iterable if condition], if condition is optional 
double = [x * 2 for x in range(1, 11)]
frui = [fru.upper() for fru in ["apple", "banana", "mango"]] 
# numb = [print(num, end=" ") for num in [1, -1, -2, 3, -3] if num >= 0]


# Match-case statement (switch): An alternative to using many "elif" statements. Execute some code if a value matches a 'case'. Benefits: cleaner and syntax is more readable 

def weekend(day):
    match day: 
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday": # '|' is the 'or'
            return False
        case "saturday", "sunday":
            return True
        case _ : # if there's no match to any cases
            return "not a day"
# print(weekend("monday"))


# MODULE = A file containing code you want to include in your program, use 'import' to include a module (built-in or your own), useful to break up a large program reusable separate files

# import math as m # 'm' here is called alias
# print(m.pi)
# from math import pi
# print(pi)


# variable scope = where a variable is visible and accessible 
# scope resolution = when using variable there's a certain order known as (LEGB) Local > Enclosed > Global > Built-in, in which we locate that variable

def fun1():
    x = 1 # enclosed
    def fun2():
        x = 2 # local, if local isn't found then enclosed would be used
        print(x)
    fun2()
# fun1()
#global
def fun3():
    print(y)
def fun4():
    print(y)
y = 3 # global 
# fun3()
# fun4()
#built-in
from math import e # built-in
def fun5():
    print(e)
e = 5 #local 
# fun5()


# if __name__ == '__main__': (this script can be imported OR run standalone) Functions and classes in this module can be reused without the main block of code executing . (dundar meaning double underscore). 
# good practice to include if __name__ == "__main__": because; code is modular, helps readability, leaves no global variables, aviod unintended execution. 
# eg. library = A Python library is a collection of pre-written code that you can reuse to perform specific tasks. Think of it as a toolbox; instead of building every tool from scratch, you simply borrow. WHEN running library directly, display a help page
# Libraries consist of modules (individual .py files) and packages (folders containing modules). Import library for functionality.


## OOPS
# object  = A "bundle" of related attributes (attributes are variables that an object has) and methods(method is a function that belongs within an object), eg. phone, cup, book, etc. You need a "class" to create many objects.
# class = (blueprint) used to design the structure and layout of an object

class car:
    def __init__(self, model, year, color, fo_sale): # def __init__(self), this is needed to create an object, called a constructor
        self.model = model # self.parameter is object
        self.year = year
        self.color = color
        self.fo_sale = fo_sale
    def drive(self): # methods of car
        print(f"Drive {self.color} {self.model}")
    def stop(self): # methods of car
        print(f"Stop {self.color} {self.model}")

# car1 = car("Supra", 2026, "wine red", False)
# print(car1) # returns memory address of the car object, where it's located
# print(car1.model) # . here is known as the attribute access operator
# car1.drive()
# car1.stop()


# Class variables = shared among all instances (objects) of a class. Defined outside the constructor. Allow you to share data among all ojects created from that class

class student:
    class_year = 2030 # class variable
    student_no = 0 
    def __init__(self, name, age):
        self.name = name # instance variable
        self.age = age
        student.student_no += 1 # accessing class variable in an object

student1 = student("Rust Cohle", 40)
student2 = student("Rust hole", 41)
# print(student1.name)
# print(student.class_year)
# print(student.student_no)


# INHERITANCE = Allows a class to inherit attributes and methods from another class. Helps with code reusability and extensibility. class Child(parent) or class sub(super)

class animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class cat(animal):
    def speak(self):
        print("meow")
class mouse(animal):
    def speak(self):
        print("chu chu")

catn = cat("Billa")
mousen = mouse("chuha")
# print(catn.name)
# catn.eat()
# catn.speak()
# print(mousen.name)
# mousen.sleep()
# mousen.speak()


# muliple inheritance = inherit from more than one parent class. C(a,b)
# multilevel inheritance = inherit from a parent which inherits from another parent. C(b) <- B(a) <- a
class animal: # parent class
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} Eating")
    def sleep(self):
        print(f"{self.name} Sleeping")

# multiple inheritance
class prey(animal): # another parent class
    def flee(self):
        print(f"{self.name} Fleeing") 

class predator(animal): # another parent class
    def hunting(self):
        print(f"{self.names} Hunting") 

class rabbit(prey): # child class
    pass  

class lion(predator):
    pass

class fish(prey, predator):
    pass

Rabbit = rabbit("kargosh")
Lion = lion("ser")
Fish = fish("machli")
#Rabbit.flee()
#Rabbit.eat()
#Lion.eat()


# super() = Function used in a child class to call methods from a parent class (superclass). Allows you to extend the functionality of the inherited methods.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    def describe(self):
        print(f"color: {self.color}\tfilled: {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
    def describe(self):
        print(f"A cirle with an area of {3.14*self.radius*self.radius}cm^2")
        super().describe() #extending the functionality
    
class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

circle = Circle("Red", True, 5)
#circle.describe()
square = Square("blue", True, 2)
#print(f"{square.width}cm")
triangle = Triangle("black", False, 3, 4)
#triangle.describe()
#print(f"{triangle.width}cm and {triangle.height}cm")


# Polymorphism = Greek word that means to "have many forms or faces". Poly = many, Morphe = form
# two ways to achieve polymorphism; 1. Inheritance = An object could be treated of the same type as a parent class. 2. "Duck typing" = Object must have necessary attributes/methods

# Inheritance 
from abc import ABC, abstractmethod
class Shape: 
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5
class Pizza(Circle):
    def __init__(self,topping,  radius):
        super().__init__(radius)
        self.topping = topping
shapes = [Circle(3), Square(5), Triangle(5,6), Pizza("pepperoni", 15)]
#for shape in shapes:
#    print(shape.area())

# Duck typing = Object must have the minimum necessary attributes/methods. "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True
class Dog(Animal):
    def speak(self):
        print("bark")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Car: # car has the minimum necessary requirements to be considered an animal
    alive = False
    def speak(self):
        print("honk")
animals = [Dog(), Cat(), Car()]
#for animal in animals:
#    animal.speak()
#    print(animal.alive)


# Static methods = A method that beong to a class rather than any object from that class (instance). Usually used for general utility functions that do not need access to class data
# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name 
        self.position = position
    def info(self): # instance method
        return f"{self.name} = {self.position}" 
    @staticmethod
    def valid_position(position): # static method
        valid_positions = ["Manager", "Chasier"]
        return position in valid_positions
employee1 = Employee("Eugeine", "Manger")
employee2 = Employee("Squidward", "Chasier")
#print(employee1.info())
#print(Employee.valid_position("Chasier"))


# Class methods = Allow operations related to the class itself. Take(cls) as the first parameter, which represents the class itself.

class Student:
    count = 0 
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa 
        Student.count += 1
        Student.total_gpa += gpa
    # Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total students: {cls.count}"
    @classmethod
    def get_average_gpa(cls):
        if cls.count ==0:
            return 0
        else:
            return f"Total gpa {cls.total_gpa/cls.count:.2f}"
    
student1 = Student("Eugeine", 9)
student2 = Student("Rick", 10)
#sprint(Student.get_count())
#sprint(Student.get_average_gpa())


# Magic methods = aka Dunder methods __init__, __str__, __eq__. They're automatically called by many of Python's built-in operations. They allow developers to define or customize the behaviour of objects

class Book:
    def __init__(self, title, author, page_no):
        self.title = title 
        self.author = author 
        self.page_no = page_no
    def __str__(self): # with this, we can return a string representation of the object when we print it directly to the console.
        return f"{self.title} by {self.author}"
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author   
    def __lt__(self, other): # lt = less than
        return self.page_no < other.page_no
    def __gt__(self, other): # gt = greater than
        return self.page_no > other.page_no
    def __add__(self, other):
        return self.page_no + other.page_no
    def __contains__(self, item):
        return item in self.title or item in self.author
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "page_no":
            return self.page_no
        else:
            return f"Key '{key}' not found"

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("Harry Potter", "J.K. Rowling", 500)
#print(book1)
#print(book2 == book3)
#print(book2 < book3)
#print(book2 > book3)
#print(book2 + book3)
#print("Hobbit" in book1)
#print(book1['title'])
#print(book1['author'])
#print(book1['page_no'])


# @property = decorator used to define a method as a property (it can be accessed like an attribute). Benefit: Add additional logic when read, write, or delete attributes. Gives you getter(to read), setter(to write), and deleter(to delete) method

class Rectangle: 
    def __init__(self, width, height):
        self._width = width 
        self._height = height 
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    @width.setter
    def width(self, n_width):
        if n_width > 0:
            self._width = n_width
        else: 
            print("Width must be greater than zero")
    @height.setter
    def height(self, n_height):
        if n_height > 0:
            self._height = n_height
        else: 
            print("Height must be greater than zero")
    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")
    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")
    
    
rectangle = Rectangle(2,4)
rectangle.width = 5
rectangle.height = 8
#del rectangle.width
#del rectangle.height
#print(rectangle.width)
#print(rectangle.height)


# Decorators = A function that extends the behaviour of another function w/o modifying the base function. Pass the base function as an argument to the decorator. 
def add_sprinkles(func):
    def wrapper(*args, **kwargs): # nested function is needed to call the decorator only when voluntarily called, without this the decorator would be called even involuntarily.
        print("added sprinkles")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
def get_icecream(flavor):
    print(f"Here is your {flavor} ice cream.")
#get_icecream("Chocolate")


# Exception = An even that interrupts teh flow of a program (ZeroDivisionError(1/0), TypeError(eg., 1+'1'), ValueError(int("string")) ). 
# 1.try, 2. except, 3. finally
'''try: 
    # try some code
except Exception: # exception catches all the errors, only use exception as a last resort. 
    # Handle an Exception
finally:
    # do some clean up'''

'''try: 
    num = int(input("enter a number "))
    print(1/num)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers.")
except Exception:
    print("Something went wrong.")
finally:
    print("Clean up.")'''


# File Detection
# for file detection we can use either relative or absolute paths. 
# Relative = folder/text.txt, Absolute = C:/Users/file/test.txt
'''import os  # Normally, a Python script only interacts with its own variables and memory. Importing the os module allows your program to "step outside" of itself and perform system-level tasks. It bridges the gap by acting as a universal translator, so you don't have to write different code for Windows and Mac.
file_path = "text.txt"
if os.path.exists(file_path):
    print(f"Location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("It's a file and not a folder")
    elif os.path.isdir(file_path):
        print("It's a directory/folder and not a file")
else:
    print("Location doesn't exist")'''

# Writing files (.txt, .json(made of keyvalue pairs), .csv(comma separated value))
txt_data = "what in the world"
file_path1 = "output.txt"
'''with open(file_path1, "w") as file: # with is a statement, used to wrap a block of code to execute, if we open a file the with statement will also close that file when we're done with it. The open function returns a file object. as file, file here is the name of the file object.
    # the second parameter is the mode, "w" is for write "x" also writes if the file doesn't exist if it does exit there'll be an error, "a" is to append a file, "r" is for read
    pass'''
# TXT 
#with open(file_path1, "w")as file:
#    file.write(txt_data)
#    print(f"text file '{file_path1}' created")
#try: 
#    with open(file_path1, "x")as file:
#        file.write(txt_data)
#        print(f"text file '{file_path1}' created")
#except FileExistsError:
#    print("file already exits")
#try: 
#    with open(file_path1, "a")as file:
#        file.write("\n" + txt_data)
#        print(f"text file '{file_path1}' created")
#except FileExistsError:
#    print("file already exits")

#JSON 
import json
employee2 = {
    "name" : "Spongebob", 
    "age" : 20, 
    "job" : "Cook"
}
file_path2 = "output2.json"
#try: 
#    with open(file_path2, "w")as file:
#        json.dump(employee, file, indent=4) #json.dump() changes the dictionary to string 
#        print(f"json file '{file_path2}' created")
#except FileExistsError:
#    print("file already exits")

#CSV
import csv
employee3 = [["Name", "Age", "Job"],["sony", 20, "cook"],["mony", 30, "unemployed"],["tony", 40, "businessman"]] 
file_path3 = "output3.csv"
#try: 
#    with open(file_path3, "w", newline="")as file:
#        writer = csv.writer(file) # writer is an object, it provides methods for providing data to a csv file
#        for row in employee3:
#            writer.writerow(row)
#        print(f"csv file '{file_path3}' created")
#except FileExistsError:
#    print("file already exits")


# READING FILES(.txt, .json, .csv)
# TXT
#try:
#    file_path4 = "output.txt"
#    with  open(file_path4, "r") as file:
#        content = file.read()
#        print(content)
#except PermissionError:
#    print("permission to this file is limited")
#JSON
#try:
#    file_path4 = "output2.json"
#    with  open(file_path4, "r") as file:
#        content = json.load(file)
#        print(content["name"]) #can access the value by its key
#except PermissionError:
#    print("permission to this file is limited")
#CVS
#try:
#    file_path4 = "output3.csv"
#    with  open(file_path4, "r") as file:
#        content = csv.reader(file) # gives memory address, to access the data we need to iterate the data line by line
#        for line in content:
#            print(line[0]) #can access lines of data through index
#except PermissionError:
#    print("permission to this file is limited")


# DATE TIME
import datetime
date = datetime.date(2025, 1, 2)
today = datetime.date.today() # today's date
time = datetime.time(12, 30, 34)
now = datetime.datetime.now() # present time
now = now.strftime("%H:%M:%S, %d-%m-%Y")


# Multithreding = Used to perform multiple tasks concurrently (multitasking). Good for I/O(input/output) bound tasks like reading files or fetching data from APIs. 
# threading.Thread(target=my_function)
import threading
import time
def walk_cat(nam):
    time.sleep(4)
    print(f"Walked {nam}")
def trash():
    time.sleep(3)
    print("trash taken out")
def mail():
    time.sleep(2)
    print("mails checked")
#chore1 = threading.Thread(target=walk_cat, args=("billa",))
#chore1.start()
#chore2 = threading.Thread(target=trash)
#chore2.start()
#chore3 = threading.Thread(target=mail)
#chore3.start()
#chore1.join() # with the join method, we'll wait for the functions to finish then execute the remaining code 
#chore2.join() 
#chore3.join()
#print("After chores execution")


# how to connect to an API
import requests
base_url = "https://pokeapi.co/api/v2/"
def get_poke_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokeman_data = response.json()
        return pokeman_data
    else:
        print(f"failed to retrieve data {response.status_code}")
pokeman_name = "pikachu"
pokeman_info = get_poke_info(pokeman_name)
if pokeman_info: 
    print(f"Name: {pokeman_info['name']}")
    print(f"Id: {pokeman_info['id']}")
    print(f"Height: {pokeman_info['height']}")