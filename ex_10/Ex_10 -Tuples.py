def file_helper(default_file):
    file_name = None

    while file_name == None:
        file_name = input("Enter file: ")
        try:
            if len(file_name) < 1:
                file_name = default_file
            file_handler = open(file_name)
        except:
            print("Invalid file name, please try again")
            file_name = None
    return file_handler


"""
Exercise 1: Revise a previous program as follows: Read and parse the “From”
lines and pull out the addresses from the line. Count the number of messages
from each person using a dictionary.

After all the data has been read, print the person with the most commits by
creating a list of (count, email) tuples from the dictionary. Then sort the
list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""
print("\n-Exercise 1-\n")
file_handler = file_helper("mbox.txt")

email_count_dict = {}
email_count_list = []

for line in file_handler:
    if line.startswith("From "):
        if line.split()[1] not in email_count_dict:
            email_count_dict[line.split()[1]] = 1
        else:
            email_count_dict[line.split()[1]] += 1

for (email, count) in list(email_count_dict.items()):
    email_count_list.append((count, email))

email_count_list.sort(reverse = True)
print(email_count_list[0])

"""
Exercise 2: This program counts the distribution of the hour of the day for
each of the messages. You can pull the hour from the “From” line by finding
the time string and then splitting that string into parts using the colon
character. Once you have accumulated the counts for each hour, print out the
counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""
print("\n-Exercise 2-\n")

file_handler = file_helper("mbox-short.txt")
hour_frequency_dictionary = {}
hour_frequency_tuple_list = []

for line in file_handler:
    if line.startswith("From "):
        hour = line.split()[5][0:2]
        if hour not in hour_frequency_dictionary:
            hour_frequency_dictionary[hour] = 1
        else:
            hour_frequency_dictionary[hour] += 1

for hour, count in hour_frequency_dictionary.items():
    hour_frequency_tuple_list.append((hour, count))


hour_frequency_tuple_list.sort()

for set in hour_frequency_tuple_list:
    print(set[0], set[1])


"""
Exercise 3: Write a program that reads a file and prints the letters in
decreasing order of frequency. Your program should convert all the input to
lower case and only count the letters a-z. Your program should not count spaces,
digits, punctuation, or anything other than the letters a-z. Find text samples
from several different languages and see how letter frequency varies between
languages. Compare your results with the tables at
https://wikipedia.org/wiki/Letter_frequencies.
"""
print("\n-Exercise 3-\n")

import string
file_handler = file_helper("mbox-short.txt")
alphabet_dictionary = {}
alphabet_tuple = []

for char in string.ascii_lowercase:
    alphabet_dictionary[char] = 0

for line in file_handler:
    for word in line.split():
        for char in word:
            try:
                alphabet_dictionary[char.lower()] += 1
            except:
                continue

for char, count in alphabet_dictionary.items():
    alphabet_tuple.append((char, count))


alphabet_tuple.sort()

for set in alphabet_tuple:
    print(set[0], set[1])
