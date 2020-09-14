print("-Exercise 1-")
"""
Exercise 1: Write a while loop that starts at the last character
in the string and works its way backwards to the first character
in the string, printing each letter on a separate line, except
backwards.
"""
print("-Exercise 1-")
word = "fruit"
for char in word[::-1]:
    print(char)

print("")
print("-Exercise 2-")
"""
Exercise 2: Given that fruit is a string, what does fruit[:] mean?
"""
print(word[:])
#contains the whole world


print("")
print("-Exercise 3-")
"""
Exercise 3: Encapsulate this code in a function named count,
and generalize it so that it accepts the string and the letter
as arguments.

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
"""
def count(string, char):
    letter_count = 0
    for letter in string:
        if letter == char:
            letter_count = letter_count + 1
    return letter_count

print(count(word, "f"))

print("")
print("-Exercise 4-")
"""
Exercise 4: There is a string method called count that is similar
to the function in the previous exercise.
Write an invocation that counts the number of times the letter a
occurs in “banana”
"""

word = "banana"
print(word.count("a"))


print("")
print("-Exercise 5-")
"""
Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string
after the colon character and then use the float function to
convert the extracted string into a floating point number.
"""

str = 'X-DSPAM-Confidence:0.8475'
print(str)
index_of_number = None
first_number = None

for char in str:
    try:
        first_number = int(char)
        index_of_number = str.find(char)
        break
    except:
        continue

print(float(str[index_of_number:]))
