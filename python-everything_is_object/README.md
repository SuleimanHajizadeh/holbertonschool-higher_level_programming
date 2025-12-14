this is readme file for Python - Everything is object




📌 Python: Everything Is an Object

Understanding how Python works internally is one of the most important skills for any Python developer.
This project explains the core ideas behind Python’s object model — how variables, references, assignments, mutability, and identity work behind the scenes.

Many beginners think:

a = 1
b = a
a = 2


means “b changes too”. It does not.

But:

l = [1, 2, 3]
m = l
l[0] = "x"


does change m.
Why? Because everything in Python is an object, and variables don’t store values—they store references.

This README explains the whole topic simply and clearly.

🧠 What You Will Learn
✔ What an object is

In Python, everything is an object: numbers, strings, lists, functions, classes, even types themselves.

✔ Class vs Object

Class = blueprint

Object/Instance = a specific item created from a class

✔ Immutable vs Mutable

Immutable objects → cannot be changed

integers, floats, strings, tuples, booleans

Mutable objects → can be changed in place

lists, dictionaries, sets

✔ What a reference is

A variable doesn’t store a value.
It stores a reference (a pointer) to an object in memory.

✔ What assignment means

a = b does not copy an object — it copies the reference.

✔ What aliasing is

Two variables referencing the same object:

l = [1, 2]
m = l    # aliasing


Changing one changes both.

✔ How to check object identity

Use is or id():

a is b
id(a) == id(b)

✔ Built-in mutable types

list

dict

set

bytearray

✔ Built-in immutable types

int

float

bool

str

tuple

frozenset

✔ How Python passes variables to functions

Python uses “pass by object reference”:

functions receive a reference to the object

mutating the object affects the original (if mutable)

reassigning inside the function does not

📚 Examples
Mutable example
l = [1, 2, 3]
m = l
l[0] = 99
print(m)  # [99, 2, 3]


Both variables point to the same list.

Immutable example
a = 5
b = a
a = 10
print(b)  # 5


a was reassigned to a new integer object; b still points to the old one.
