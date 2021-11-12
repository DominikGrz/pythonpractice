# imports
import threading
import time
import math
import os
import sys
import random
import shutil

from colorama import Fore
from colorama import Back
from colorama import Style

# hide cursor logic
if os.name == 'nt':
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]
def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
hide_cursor()
# clear junk
os.system('clear')
# spacer
print(f" {Fore.CYAN}")

#*02-------------------------------------------------------------------------
#? variables

#name = "thisname"
#name_last = "thatname"
#full_name = name +" "+ name_last
#print("Hello " + full_name)

#age = 22
#age += 1
#print("Age: " + str(age))

#height = 250.5
#print("height: " + str(height) + "cm" )

#booool = True
#print(booool)
#print("are u: " + str(booool))

#*03-------------------------------------------------------------------------
#? multiple assignments

#name, age, state = "the name", 21, False
#numba_one, number_two, nr_three = "22"

#*04-------------------------------------------------------------------------
#? string methods

#stringg = "wowowowowwow wow"
#print(stringg.find("o"))
#print(stringg.upper())
#print(str(stringg.count("o"))+" "+str(stringg.count("wow")))
#print(stringg.replace("wow"," damn "))
#print(stringg*2)

#*05-------------------------------------------------------------------------
#? type casting

#x = 1 #int
#y = 2.0 #float 
#z = "3" #str

#x = float(z)
#y = str(y)
#z = int(z)

#print(x)
#print(y)
#print(z)

#*06-------------------------------------------------------------------------
#? user input

#thename = input("What is name: ")
#yournumber = int(input("What your number: "))
#print("Wow name is: " + thename + " and number is: " + str(yournumber))

#*07-------------------------------------------------------------------------
#? MATH

#pi = 3.14
#b = 4
#z = 20
#print(round(pi))
#print(math.ceil(pi))
#print(max(pi,b,z))

#*08-------------------------------------------------------------------------
#? string slicing

#longstring = "asdiasd ADASDAD asdasd odadasdasddas"
#firstword = longstring[:7]
#lastword = longstring[23:]
#stepword = longstring[::3]
#longbackward = longstring[::-1]
#print(firstword)
#print(lastword)
#print(stepword)
#print(longbackward)

#weburl = "http://google.com/"
#webur2 = "http://wikipedia.com/"
#slice = slice(7,-5)
#print(weburl[slice])
#print(webur2[slice])

#*09-------------------------------------------------------------------------
#? if statements

#age = int(input("How old are you: "))
#if age == 100:
#    print("You are a century old")
#elif age >= 18:
#    print("You are an adult")
#elif age < 0:
#    print("Invalid input")
#else: 
#    print("You are a child")

#*10-------------------------------------------------------------------------
#? logical operators - and, or, not<- the same as other lang

#temp = int(input("What is temperature: "))
#if temp>=0 and temp<=30:
#    print("the temp is ok")
#elif temp < 0 or temp>30:
#    print("its hell")

#*11-------------------------------------------------------------------------
#? while loop

#while 0:
#    print("why")
#name = None
#while not name:
#    name = input("what name: ")

#*12-------------------------------------------------------------------------
#? for loop

#for i in range(10):
#    print(i)
#for i in range(50,100+1):
#    print(i)
#for i in "string wow":
#    print(i)
#for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1)

#*13-------------------------------------------------------------------------
#? nested loop

#rows = int(input("Rows: "))
#columns = int(input("Columns: "))
#symbol = str(input("Symbol: "))

#ez way
#for i in range(rows):
#    print(symbol*columns)

#nested way
#for i in range(rows):
#    for j in range(columns):
#        print(symbol, end="")
#    print()

#*14-------------------------------------------------------------------------
#? loop control statements - break, continue, pass

#while True:
#    name = input("Enter name man: ")
#    if name != "":
#        break
        
#telnumber = "123-123-3212"
#for i in telnumber:
#    if i == "-":
#        continue
#    print(i, end="")

#*15-------------------------------------------------------------------------
#? list

#food = ["pizza","burger","durum"]
#print(food)
#food[1] = "hamburger"
#print(food)
#food.append("doner")
#print(food)

#*16-------------------------------------------------------------------------
#? multi dim list - list of lists

#drinks = ["tea","soda","milkshake"]
#food = ["pizza","hamburger","hotdog"]
#vegetable = ["cucumber","carrot","onion"]
#things = [drinks, food, vegetable]
#print(things)
#print(things[2])
#print(things[1][1])

#*17-------------------------------------------------------------------------
#? tuple - collection which is ordered and unchangeable

#student = ("his name", 20, "is male")
#print(student.count("his name"))
#print(student.index("is male"))

#*18-------------------------------------------------------------------------
#? set - collection which is unordered, unindexed, has no duplicates

#utensils = {"pencil", "fork", "spoon"}
#utensils.add("knife")
#utensils.remove("pencil")
#dishes = {"bowl", "plate", "cup"}
#utensils.update(dishes)
#table = utensils.union(dishes)
#for x in utensils:
#    print(x)
#for x in table:
#    print(x)

#*19-------------------------------------------------------------------------
#? dictionary - collection which is changeable, unordered with unique 
#?              key:value pairs - also fast because of hashing

#capitals = {'Germany':'Berlin','Poland':'Warszawa','Czechia':'Prague'}

#print(capitals.get('Germany'))
#print(capitals.get('USA'))
#print(capitals.values())
#print(capitals.keys())
#print(capitals.items())

#capitals.update({str(input("The country: ")):str(input("The capitol: "))})
#capitals.pop('Czechia')
#for key,value in capitals.items():
#    print(key, value)


#*20-------------------------------------------------------------------------
#? indexing operator [] - access sequence's element (ex. str,list,tuples)

#name = "wow a name"
#if(name[0].islower()):
#    name = name.capitalize()
    
#! fun - find the first name and the last name // edited with functions and return values

full_name = str(input("What is your full name?: "))

#iterate thru string until space
def get_first_word(givestring):
    tempword = ""
    for key in givestring:
        if key == " ":
            break
        tempword += key
    return str(tempword)

print("Your first name: "+get_first_word(full_name))
print("Your family name: "+ get_first_word(full_name[::-1])[::-1])



#*21-------------------------------------------------------------------------
#? funtions - man u know what it do

#def wowfunction():
#    print("it do be printing tho")

#*22-------------------------------------------------------------------------
#? return values - pog also it have positional arguments

#def wowfunction(x):
#    return "it "+str(x)+" be printing tho"

#haha = "do"
#print(wowfunction(haha))

#*23-------------------------------------------------------------------------
#? keyword arguments - it do not be positional

#def wowfunction(x, y, z):
#    print("it "+str(x)+" be "+ y +" "+ z)

#ha = "do"
#haha = "printing"
#sheesh = "tho"
#wowfunction(z=sheesh, x=ha, y=haha)

#*24-------------------------------------------------------------------------
#? nested function calls - function in function wow

#print(round(abs(float(input("input numba: ")))))

#*25-------------------------------------------------------------------------
#? viable scope - actually important - it work only in region it be created
#? LEGB - Local first - Enclosing second - Global third - Built-in last
#? that be it tho

#*26-------------------------------------------------------------------------
#? *args - parameter will pack all arguments into a tuple

#def add(*numbers):
#    asum = 0
#    numbers = list(numbers)
#    for i in numbers:
#        asum += i
#    return asum

#print(add(1,5,1,2,6,8,9,))

#*27-------------------------------------------------------------------------
#? **kwargs - first of all wtf - second the same but instead of tuple it
#?            packs into a dictionary that can accept keyword arguments

#def hello(**words):
#    print("These were the words " +words['lastword'] + words['firstword'])
#hello(firstword=" sheesh", lastword="dripcheck")

#def displayEverything(**alles):
#    for key,value in alles.items():
#        print(value ,end=" ")
#    print(" ")
#displayEverything(first="man",second="went",third="into", fourth="a", fifth="store", sixth="today")

#*28-------------------------------------------------------------------------
#? str.format() - optional gives more control

#varrr = "it do be"
#errrr = "why not"
#pogstatement = "{secondly} eat some soup, {firstly} very tasty {firstly}"

#print("{} eat some soup, {} very tasty ".format(errrr, varrr)) #! actually kinda nice
#print("{1} eat some soup, {0} very tasty ".format(varrr, errrr)) #! damn son - positional argument
#print(pogstatement.format(secondly="why not", firstly="it do be")) #! dayum - keyword argument

#name = "amuchname"
#print("hello {:10} sheesh".format(name))
#print("hello {namer:<15} sheesh".format(namer=name))
#print("hello {:>15} sheesh".format(name))
#print("hello {:^15} sheesh".format(name))

#pi = 3.14159
#numba = 79327
#print("pi is {:.3f}".format(numba))
#print("pi is {:,}".format(numba))
#print("pi is {:b}".format(numba))
#print("pi is {:o}".format(numba))
#print("pi is {:X}".format(numba))
#print("pi is {:e}".format(numba))

#*29-------------------------------------------------------------------------
#? random wow 

#x = random.randint(1,100)
#print(x)

#funky stuff
#while 1:
#    print(random.randint(10,99), end="\r")
#    time.sleep(0.1)

#mylist = ['rock', 'paper', 'scissors']
#y = random.choice(mylist)
#print(y)

#cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
#random.shuffle(cards)

#*30-------------------------------------------------------------------------
#? exception - interruption the flow of a program
#try:
#    pass
#except ValueError: #catches specific exception
#    pass
#else:
#    pass
#finally:
#    pass

#*31-------------------------------------------------------------------------
#? file detection

#path = ""
#
#if os.path.exists(path):
#    print("yes")
#    if os.path.isfile(path):
#        print("that a file")
#    if os.path.isdir(path):
#        print("that a dir")
#else:
#    print("no")

#*32-------------------------------------------------------------------------
#? read a file

#try:
#    with open('text.txt') as file:
#        print(file.read())
#except FileNotFoundError:
#    print("cant find")


#*33-------------------------------------------------------------------------
#? write a file 'w' overwrite, 'a' append

#text = "Sheeeeeeesh.\nDamn."
#with open('text.txt','a') as file:
#    file.write(text)


#*34-------------------------------------------------------------------------
#? copyfile() - copies contents of a file
#? copy() - copyfile() + permission mode + destination can be a dir
#? copy2() - copy() + copies metadata (file creation and modif times)

#shutil.copy2('text.txt','textcopied.txt')


#*35-------------------------------------------------------------------------
#? move a file/dir

#src = "textcopied.txt"
#to = "/Users/dominikgrzesik/Desktop/text.txt"

#try:
#    if os.path.exists(to):
#        print("already there")
#    else:
#        os.replace(src,to)
#except FileNotFoundError:
#    print(src+" not found")

#*36-------------------------------------------------------------------------
#? delete a file/dir

#path = "text copy.txt"
#try:
#    #os.remove(path)
#    #os.rmdir(path)
#    shutil.rmtree(path) #dangerous
#except FileNotFoundError:
#    print("That file doesn't exist")
#except PermissionError:
#    print("No permission")
#except OSError:
#    print("u just cant do that")
#else:
#    print(path+" was deleted")

#*37-------------------------------------------------------------------------
#? module - file containing pyhton code, seperate scope
#import messages as msg

#msg.hi()
#msg.bye()


#*38-------------------------------------------------------------------------
#? rock paper scissors
#def result(plr,com,game):
#    print("player: "+plr)
#    print("computer: "+com)
#    print("Result: "+game+"!")

#while True:
#    choices = ["rock","paper","scissors"]
#    computer = random.choice(choices)
#    player = None
#    while player not in choices:
#        player = input("rock, paper or scissors?: ").lower()
#    if player == computer:
#        result(player,computer,"draw")
#    if player == "rock":
#        if computer == "scissor":
#            result(player,computer,"win")
#        if computer == "paper":
#            result(player,computer,"lose")
#    elif player == "paper":
#        if computer == "rock":
#            result(player,computer,"win")
#        if computer == "scissor":
#            result(player,computer,"lose")
#    elif player == "scissor":
#        if computer == "paper":
#            result(player,computer,"win")
#        if computer == "rock":
#            result(player,computer,"lose")

#*39-------------------------------------------------------------------------
#? basic quiz game - it boring tho

#*40-------------------------------------------------------------------------
#? POOP - python object oriented programming

#class Car:
#    def __init__(self, make, model, year, color):
#        self.make = make
#        self.model = model
#        self.year = year
#        self.color = color
#    def drive(self):
#        print(self.model+" drive")
#    def stop(self):
#        print(self.model+" stop")

#car1 = Car("whatever","GTR","1988","white")
#print(car1.color)
#car1.drive()
#car1.stop()

#*41-------------------------------------------------------------------------
#? class variables/instance variables

#class Car:
#    wheels = 4 # class variable
#    def __init__(self, make, model, year, color):
#        self.make = make    # vvv instance variables
#        self.model = model
#        self.year = year
#        self.color = color

#car1 = Car("whatever","GTR","1988","white")
#car2 = Car("whatevs","CTR","988","black")

#car2.wheels = 2

#print(car1.wheels)
#print(car2.wheels)

#Car.wheels = 3
#car3 = Car("BMW","R69","2220","red")
#print("")
#print(car1.wheels)
#print(car2.wheels)
#print(car3.wheels)

#*42-------------------------------------------------------------------------
#? inheritance - parent/child relationship (child inherits of its parent)

#class Animal:
#    alive = True
#    def eats(self):
#        print("he eat")
#    def sleeps(self):
#        print("he sleep")
#class Rabbit(Animal):
#    def run(self):
#        print("he do be hoppin")
#class Fish(Animal):
#    def swim(self):
#        print("he do be swimin")
#class Hawk(Animal):
#    def fly(self):
#        print("he do be flyin")

#rabbit = Rabbit()
#fish = Fish()
#hawk = Hawk()

#print(rabbit.alive)
#hawk.sleeps()
#fish.eats()

#hawk.fly()
#fish.swim()


#*43-------------------------------------------------------------------------
#? multilevel inheritance - the same just with children of children(parent) of parent(and so on)
#? organism -> animal -> dog
#? machine -> vehicle -> car -> cartype etc

#*44-------------------------------------------------------------------------
#? multiple iheritance - almost the same just with 2 parents(inherits all functions etc)
#? classes prey, predator
#? hawk->predator fish->prey,predator example

#*45-------------------------------------------------------------------------
#? method overriding

#class Animal:
#    def eat(self):
#        print("it be eatin")
#class Rabbit(Animal):
#    def eat(self):
#        print("this rabbit be eatin")
#rabbit = Rabbit()
#rabbit.eat()

#*46-------------------------------------------------------------------------
#? method chaining - 


#*47-------------------------------------------------------------------------
#?

#*48-------------------------------------------------------------------------
#?

#*49-------------------------------------------------------------------------
#?

#*50-------------------------------------------------------------------------
#?

#*51-------------------------------------------------------------------------
#? walrus operator :=

#happy = True
#print(happy)
#print(happy := True)

#foods = list()
#while True:
#    food = input("u like?: ")
#    if food == "quit":
#        break
#    foods.append(food)

#foods = []
#while food := input("u ike wha?: ") != "quit":
#    foods.append(food)


#*52-------------------------------------------------------------------------
#? functions to variables - mindblown

#def hello():
#    print("Hello")
#hi = hello
#hello()
#hi()

#say = print
#say("shieeet")

#*53-------------------------------------------------------------------------
#?  higher order function - it either 1. accepts a function as an argument
#?                                    or
#?                                    2. returns a function (python treats as object)
#* 1.-----
#def loud(text):
#    return text.upper()
#def quiet(text):
#    return text.lower()
#def hello(func):
#    print(text := func("Hello"))
#hello(quiet)
#* 2.-----
#def divisor(x):
#    def dividend(y):
#        return y/x
#    return dividend
#divide = divisor(3)    
#print(divide(21)) 

#*54-------------------------------------------------------------------------
#? lambda function - function written in 1 line using lambda keyword (shortcut)

#double = lambda x:x*2
#multiply = lambda x, y: x * y
#add = lambda x,y,z: x + y + z
#full_name = lambda first_name, last_name: first_name+" "+last_name
#age_check = lambda age:True if age >= 18 else False

#print(age_check(120))
#print(add(10,2,4))
#print(multiply(10,20))
#print(double(10))

#*55-------------------------------------------------------------------------
#? sort() method   - lists
#? sorted() / sort() function - iterables
#? why ^^

#students = ["asda","wows","sick","damn"]
#students.sort(reverse=True)
#for i in students:
#    print(i)

#students = ("asda","wows","sick","damn")
#sorted_students = sorted(students,reverse=True)
#for i in students:
#    print(i)

#students = (("squid","F", 29),
#            ("sand","A",20),
#            ("man","C",1),
#            ("pogger","B",4))

#index = lambda indexe:indexe[1]
#sorted_students = sorted(students,key=index,reverse=True)

#for i in sorted_students:
#    print(i)

#*56-------------------------------------------------------------------------
#? map() - applies a function to each item in an iterable (list, tuple)

#store = [("shit",20.50),
#         ("golden shit", 21.00),
#         ("a sock", 40.00),
#         ("mouse", 120.00)]
#to_euro = lambda dollar: (dollar[0],round(dollar[1] * 0.82,2))
#store_euros = list(map(to_euro, store))
#for i in store_euros:
#    print(i)

#*57-------------------------------------------------------------------------
#? filter()

#store = [("shit",20),
#         ("golden shit", 21),
#         ("a sock", 40),
#         ("mouse", 12)]

#age = lambda data:data[1] >= 18

#asda = list(filter(age, store))
#for i in asda:
#    print(i)

#*58-------------------------------------------------------------------------
#? reduce() - apply function to an iterable and reduce it to a single
#?            cumulative value - first two elements until 1 remain

#import functools

#letters = ["A","B","C","D","E"]
#result = functools.reduce(lambda x,y:x+y,letters)
#print(result)

#factorial = [10,9,8,7,6,5,4,3,2,1]
#result = functools.reduce(lambda x,y:x*y,factorial)
#print(result)


#*59-------------------------------------------------------------------------
#? list comprehension - create a list with less syntax

#squared = [i * i for i in range(1,10)]
#print(squared)

#students = [100,90,80,70,60,50,40,30,20,10,0]
#passed_students = [i for i in students if i >= 60]
#print(passed_students)

#students = [100,90,80,70,60,50,40,30,20,10,0]
#passed_students = [i if i >= 60 else "FAILED" for i in students]
#print(passed_students)


#*60-------------------------------------------------------------------------
#? dictonary comprehension - create dictionary using an expression
#?                           can replace for loops and certain lambda funcs

#citiesImperial = {'NY':32,'Boston':75,'LA':100,'Chicago':50}
#citiesMetric = {key: round((value-32)*(5/9)) for (key,value) in citiesImperial.items()}
#print(citiesMetric)

#! continue saved for later use case seems doesnt seem to be needed asap

#*61------------------------------------------------------------------------
#? zip(*iterables) - aggregate elements from two or more iterables (list, tuples, sets, etc.)
#?                   creates a zip object with paired elements stored in tuples for each element
#?                   within the zip object

#usernames = ["dude","what","why"]
#passwords = ("pass","word","wow")
#points = ["10","69","420"]

#users = dict(zip(usernames, passwords))
#for key,value in users.items():
#    print(key+" : "+value)

#users = zip(usernames,passwords,points)
#for i in users:
#    print(i)


#*62------------------------------------------------------------------------
#? if __name__ == '__main__':  ?#
#! important
 
#? y tho?
#? 1. Module can be run run as a standalone program
#? 2. Module can be imported and used by other modules

#? Python interpreter sets "special variables", one of which is __name__
#? Python will assign the __name__ variable a value of '__main__' if it's
#? the initial module being run

#import messages

#print(__name__)
#print(messages.__name__)

#if __name__ == '__main__':
#    print("running this directly")
#else:
#    print("running other indirectly")
 
#def wowow():   #! for messages bein able to import this, all other import should be there aswell?
#    print("hello")

#if __name__ == '__main__':
#    pass


#*63-------------------------------------------------------------------------
#? time module

#print(time.ctime(0)) # convert a time expressed in seconds since epoch to readable string
                     # epoch is form 1970(when your computer thinks time began)
#print(time.time())   # return current seconds since epoch
#print(time.ctime(time.time())) # will get current time

#time_obj = time.localtime()
#print(time_obj)

#local_time = time.strftime("%H:%M:%S %A %B %Y", time_obj)
#print(local_time)

#time_str = "20 April, 2020"
#time_obj2 = time.strptime(time_str,"%d %B, %Y")
#print(time_obj2)

#time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
#time_str = time.asctime(time_tuple)
#print(time_str) # Mon Apr 20 04:20:00 2020

#time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
#time_str = time.mktime(time_tuple)
#print(time_str) # 1587352800.0 since epoch date

#! wow threading so cooooool
#*64-------------------------------------------------------------------------
#? threading
#? thread - a flow of execution, seperate order of instructions
#?          however each thread takes a turn running to achieve concurrency 
#?          (concurrently != parallel)
#?          GIL = global interpreter lock
#?          allows only one thread to hold the control of the Python interpreter at any one time

#? cpu bound - program/task spends most of it's time waiting for internal events (CPU internal)
#?             use multiprocessing

#? io bound  - program/task spends most of it's time waiting for external events (user input)
#?             use multithreading

#print(threading.active_count())
#print(threading.enumerate())

#def eat_something():
#    time.sleep(3)
#    print("eaten")

#def drink_tee():
#    time.sleep(4)
#    print("drank")

#def study():
#    time.sleep(5)
#    print("learned")

#x = threading.Thread(target=eat_something, args=()) # these are all seperate of the main thread
#x.start()

#y = threading.Thread(target=drink_tee, args=())
#y.start()

#z = threading.Thread(target=study, args=())
#z.start()

#x.join()
#y.join()
#z.join()

#eat_something()
#drink_tee()
#study()
#print(time.perf_counter())

#-------------------------------------------------------------------------
#? daemon thread - a thread that runs in the background, not important for program to run
#?                 your program will not wait for deamon threads to complete before exiting
#?                 non-deamon threads cannot normally be killed, stay alive until task is complete
#?                 ex. background tasks, garbage collection, waiting for input, long running process

#def timer():
#    print()
#    count = 0
#    while True:
#        time.sleep(1)
#        count += 1
#        print("logged in for "+str(count)+"s" )

#x = threading.Thread(target=timer, daemon=True)
#x.start()

#answer = input("stop? y/n")



#-------------------------------------------------------------------------
#?


#-------------------------------------------------------------------------
#?


#-------------------------------------------------------------------------
#?


#-------------------------------------------------------------------------
#?


#-------------------------------------------------------------------------
#?







print(" ")
