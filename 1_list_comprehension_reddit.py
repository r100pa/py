'''
I wanted to exercise list comprehensions in Python.
Some googling and I found that not only me was looking for this challenge :)
www.reddit.com/r/learnpython/comments/4d2yl7/i_need_list_comprehension_exercises_to_drill/

So, my solutions:
'''

#   Find all of the numbers from 1-1000 that are divisible by 7
divisible_by_7 = [num for num in range(1,1001) if num % 7 == 0]

#   Find all of the numbers from 1-1000 that have a 3 in them
have3 = [num for num in range(1,1001) if "3" in str(num)]

#    Count the number of spaces in a string
def count_spaces(s):
    return  len([char for char in s if char == " "])

#    Remove all of the vowels in a string
def remove_vowels(s):
    return [char for char in s if char not in "aeiouy"]
    
#    Find all of the words in a string that are less than 4 letters
def find_shorter_than4(s):
    return [word for word in s.split() if len(word) < 4]

#    Use a dictionary comprehension to count the length of each word in a sentence.
def length_of_words(s):
    return {word:len(word) for word in s.split()}

#    Use a nested list comprehension to find all of the numbers from 1-1000 that
#    are divisible by any single digit besides 1 (2-9)
divisible = [num for num in range(1,1001) if [div for div in range(2,10) if num % div == 0]]
print(divisible)

#    For all the numbers 1-1000, use a nested list/dictionary comprehension to
#    find the highest single digit any of the numbers is divisible by

highest_divisor = {num:max(div for div in range(2,10) if num % div == 0) for num in range(1,1001) if [div for div in range(2,10) if num % div == 0]}
print(highest_divisor)                   


'''
I think I get it ;)
'''

