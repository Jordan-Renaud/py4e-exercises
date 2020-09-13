"""
Write a program that repeatedly prompts a user for
integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest
of the numbers. If the user enters anything other than a valid
number catch it with a try/except and put out an appropriate message
and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""

#set global variables as empty containers.
largest = None
smallest = None

#start while loop to run until user enters "done"
while True:
    #asks for input
    num_raw = input("Enter a number: ")

    #try/except condition to check for words vs integers
    try:

        #converts string num into an integer
        num = int(num_raw)

        #sets largest and smallest to the first number entered
        if largest == None or smallest == None:
            largest = num
            smallest = num

        #checks to see if largest is largest and smallest is smallest
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    except:
        #ends program if user enters done
        if num_raw == "done": break
        #deals with strings that dont convert
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
