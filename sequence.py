# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter three numbers: start, stop, and step.
    Create a range object using these values and convert it to a list named 'numbers'.

    TIP: Use the range(start, stop, step) function and list() to convert it to a list.
"""

### Your code here
# start = int(input('Enter start: '))
# stop = int(input('Enter stop: '))
# step = int(input('Enter step: '))

# numbers = list(range(start, stop, step))
# print(f'Generated list: {numbers}')
### EXPECTED OUTPUT:
# Enter start: 2
# Enter stop: 10
# Enter step: 2
# Generated list: [2, 4, 6, 8]

# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a list of numbers separated by spaces.
    Then, ask for two indices 'start' and 'end' to slice the list.
    Create a new list 'sliced_list' containing elements from 'start' to 'end' (excluding 'end').

    TIP: Use list slicing syntax list[start:end] to extract a sublist.
"""

### Your code here
# user_input = input('Enter numbers separated by space')
# input_list = list(map(int, user_input.split()))

# start_index = int(input('Enter start index: '))
# stop_index = int(input('Enter stop index: '))

# sliced_list = input_list[start_index:stop_index]
# print (f'Sliced list: {sliced_list2}')
### EXPECTED OUTPUT:
# Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9
# Enter start index: 2
# Enter end index: 6
# Sliced list: [3, 4, 5, 6]

# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Write a program that generates a list of numbers from 1 to 50 using range().
    Then, create a new list 'evens' that contains only the even numbers from this list using slicing.

    TIP: Use range(start, stop) to create the initial list.
        Use slicing with a step to extract every second element.
"""

### Your code here
# original_list = range(1,51)
# print (f'Original List: {list(original_list)}')
# print (f'Even Numbers: {list(original_list[1:51:2])}')
### EXPECTED OUTPUT:
# Original list: [1, 2, 3, ..., 50]
# Even numbers: [2, 4, 6, ..., 50]

# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Write a program that generates a list of numbers from 100 to 50 (inclusive), counting down by 5.
    Then, create a new list 'first_half' that contains only the first half of this list using slicing.

    TIP: Use range(start, stop, step) to create the initial list.
        Use slicing to extract the first half.
"""

### Your code here
# orig_list = range(100,49,-5)
# print (f'Original list: {list(orig_list)}')
# print (f'First half: {list(orig_list[:6])}')
### EXPECTED OUTPUT:
# Original list: [100, 95, 90, ..., 50]
# First half: [100, 95, 90, ..., 75]

# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a word.
    Create a new string 'reversed_word' that contains the word in reverse order using slicing.

    TIP: Use slicing with a negative step to reverse a string.
"""

### Your code here
# word_input = input('Enter a word: ')
# print (word_input[::-1])
### EXPECTED OUTPUT:
# Enter a word: Python
# Reversed word: nohtyP

# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
    Write a program that generates a list of numbers from 10 to 100 with a step of 10.
    Then, create a new list 'middle_part' containing all elements except the first and last two using slicing.

    TIP: Use range(start, stop, step) to create the initial list.
         Use slicing to remove the first and last two elements.
"""

### Your code here
# orig_l = range(10,101,10)
# print (f'Original list: {list(orig_l)}')
# print (f'Middle part: {list(orig_l[2:8])}')
### EXPECTED OUTPUT:
# Original list: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Middle part: [30, 40, 50, 60, 70, 80]

# ---------------------------------- Task 7 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a sentence.
    Create a new string 'every_second_char' that contains every second character from the sentence using slicing.

    TIP: Use slicing with a step to extract every second character.
"""

### Your code here
# sentence_input = input('Enter a sentence: ')
# print (f'Every second character: {sentence_input[::2]}')
### EXPECTED OUTPUT:
# Enter a sentence: Python slicing is powerful!
# Every second character: Pto lcn spwru!

# ---------------------------------- Task 8 ---------------------------------- #
""" DESCRIPTION:
    Write a program which will ask the user to enter 3 names.
	The names, should be stored into a list 'names'.
    Create another list 'sorted_names' which will have names, sorted alphabetically. Do not change the original 'names' list.

    TIP: use list.sort() method to sort a list. Note, that the sort() method works "in-place",
"""

### Your code here
names = []

names.append(input('Enter 1st name: '))
names.append(input('Enter 2nd name: '))
names.append(input('Enter 3rd name: '))

sorted_names = names[:]
sorted_names.sort()
print (f'Originally entered names {names}')
print (f'Sorted name: {sorted_names}')


### EXPECTED OUTPUT:
# Enter 1st name: Maria
# Enter 2d name: Ivan
# Enter 3d name: Asen

# Originally entered names:  ['Maria', 'Ivan', 'Asen']
# Sorted names: ['Asen', 'Ivan', 'Maria']

# ---------------------------------- Task 9 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a word and then checks if the word is a palindrome.
    A palindrome is a word that reads the same forward and backward, ignoring case.

    Tip: you can use str.lower() to convert a string to lowercase
"""

### Your code here

### EXPECTED OUTPUT:
# Enter a word : Racecar
# The word 'Racecar' is a palindrome

# Enter a word : car
# The word 'car' is not a palindrome