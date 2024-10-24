## 👉 Day 32 Challenge
# List
- Create a list that stores greetings in different languages. Start with the language you speak.
- Then, go on the internet to find other greetings in other languages. Here is a list of greetings to get you started.
- Import random library. Generate a random number between 0 and maximum number of items in your list.
- At random, when the user clicks run, print one of the greetings.
- Use an f-string.


### Lists in Programming

A **list** is a data structure used to store multiple items in a single variable. Lists are widely used in programming because they allow for storing, accessing, and manipulating collections of data. Lists are dynamic, which means they can grow and shrink during runtime. They can also store elements of different data types, such as numbers, strings, and even other lists.

### Syntax (in Python):

### Creating a List
A list is defined by placing elements inside square brackets `[]`, separated by commas.
Accessing List Elements
You can access elements of a list using indices, starting at 0 for the first element.

```python
# Example of a simple list
my_list = [1, 2, 3, 4, 5]

# Example of a mixed-type list
mixed_list = [10, "apple", 3.14, True]


# Accessing the first element
first_element = my_list[0]  # Output: 1

# Accessing the second element
second_element = my_list[1]  # Output: 2
Modifying List Elements
You can modify elements in a list by assigning new values to specific indices.


# Changing the first element
my_list[0] = 100  # my_list is now [100, 2, 3, 4, 5]
Adding Elements to a List
You can append new elements to the list using the append() method.


# Adding a new element to the end
my_list.append(6)  # my_list is now [100, 2, 3, 4, 5, 6]
Removing Elements from a List
Elements can be removed using the remove() or pop() methods.


# Removing the first occurrence of a value
my_list.remove(100)  # my_list is now [2, 3, 4, 5, 6]


