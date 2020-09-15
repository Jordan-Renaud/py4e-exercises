"""
Exercise 1: Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None. Then write a function
called middle that takes a list and returns a new list that contains all but
the first and last elements.
"""
print("\n-Exercise 1- \n")

def chop(your_list):
    your_list = your_list[1:len(your_list) - 1]
    print("function chop returns nothing but does this: ", your_list)

def middle(your_list):
    return [your_list[0], your_list[len(your_list) - 1]]

test_list = ["apple", "banana", "carrot", "date"]
print(chop(test_list))
print("function middle:", middle(test_list))

"""
Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt.
Write a program to open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word is
not in the list, add it to the list. When the program completes, sort and
print the resulting words in alphabetical order.
"""
print("\n-Exercise 4- \n")

file_handler = open("romeo.txt")
romeo_string = ""
romeo_but_organised = []

for line in file_handler:
    romeo_string += line

for word in romeo_string.strip().split():
    if word not in romeo_but_organised:
        romeo_but_organised.append(word)

romeo_but_organised.sort()
print(romeo_but_organised)


"""
Exercise 5: Write a program to read through the mail box data and when you
find line that starts with “From”, you will split the line into words using
the split function. We are interested in who sent the message, which is the
second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line and print out the second word for each From line,
then you will also count the number of From (not From:) lines and print out a
count at the end. This is a good sample output with a few lines removed:

python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
"""
print("\n-Exercise 5- \n")
file_name = None

while file_name == None:
    try:
        file_name = input("Enter file name: ")
        if len(file_name) < 1 : file_name = "mbox-short.txt"
        file_handler = open(file_name)
    except:
        print("Invalid file address, please try again")
        file_name = None
count = 0

for line in file_handler:
    if line.startswith("From:"):
        count += 1
        print(line.strip().split(": ")[1])

print("There were", count, "lines in the file with From as the first word")


"""
Exercise 6: Rewrite the program that prompts the user for a list of numbers
and prints out the maximum and minimum of the numbers at the end when the
user enters “done”. Write the program to store the numbers the user enters
in a list and use the max() and min() functions to compute the maximum and
minimum numbers after the loop completes.

Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
"""
print("\n-Exercise 6- \n")

new_input = ""
num_list = []

while new_input != "done":
    new_input = input("Enter a number: ")
    try:
        num_list.append(float(new_input))
    except:
        print("Invalid input, please try again")

print("Maximum:", max(num_list))
print("Minimum:", max(num_list))
