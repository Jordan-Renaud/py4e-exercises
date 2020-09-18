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
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in
a dictionary. It doesn’t matter what the values are. Then you can use the in
operator as a fast way to check whether a string is in the dictionary.
"""
print("\n-Exercise 1-\n")

file_handler = file_helper("words.txt")

word_dict = dict()
for line in file_handler:
    for word in line.split():
        if word not in word_dict:
            word_dict[word] = "value"

print(word_dict)


"""
Exercise 2: Write a program that categorizes each mail message by which day of
the week the commit was done. To do this look for lines that start with “From”,
then look for the third word and keep a running count of each of the
days of the week. At the end of the program print out the contents of your
dictionary (order does not matter).

Sample Line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Sample Execution:

python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""
print("\n-Exercise 2-\n")

file_handler = file_helper("mbox-short.txt")
week_count_dict = {}

for line in file_handler:
    if line.startswith("From "):
        if line.split()[2] not in week_count_dict:
            week_count_dict[line.split()[2]] = 1
        else:
            week_count_dict[line.split()[2]] += 1

print(week_count_dict)

"""
Exercise 3: Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from each email
address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""
print("\n-Exercise 3-\n")

file_handler = file_helper("mbox-short.txt")

email_count_dict = {}

for line in file_handler:
    if line.startswith("From "):
        if line.split()[1] not in email_count_dict:
            email_count_dict[line.split()[1]] = 1
        else:
            email_count_dict[line.split()[1]] += 1

print(email_count_dict)

"""
Exercise 4: Add code to the above program to figure out who has the most
messages in the file. After all the data has been read and the dictionary
has been created, look through the dictionary using a maximum loop (see
Chapter 5: Maximum and minimum loops) to find who has the most messages and
print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""
print("\n-Exercise 4-\n")

largest = None
largest_email_key = None

for email in email_count_dict:

    if largest == None:
        largest = email_count_dict[email]
        largest_email_key = email

    elif email_count_dict[email] > largest:
        largest = email_count_dict[email]
        largest_email_key = email

print("Most messages sent by:", largest_email_key, "who sent", largest, "emails.")


"""
Exercise 5: This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from (i.e., the
whole email address). At the end of the program, print out the contents of
your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""
print("\n-Exercise 5-\n")

file_handler = file_helper("mbox-short.txt")

domain_count_dict = {}
largest = None
largest_email_key = None

#looks through each line in file and pulls out the line with the email in.
for line in file_handler:
    if line.startswith("From "):
        #finds the email address
        email = line.split()[1]
        #finds the domain to the email
        email_domain = email[email.find("@"):]
        if email_domain not in domain_count_dict:
            domain_count_dict[email_domain] = 1
        else:
            domain_count_dict[email_domain] += 1

print(domain_count_dict)
