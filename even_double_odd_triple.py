# Ken Leam G. Gamboa
# BSCPE 1-5
# This program identifies the even/odd numbers from a text file,
# will get the square of each even number,
# will get the cube of each odd number,
# and will append the numbers in their respective text files.

# open integer.txt, open double.txt, open triple.txt
with open ("integer.txt", "r") as integer_file, open("double.txt", "a") as double_file, open("triple.txt", "a") as triple_file: 
    #for each line in nembers.txt
    for line in integer_file:
        #convert each number in the line into integers
        num_in_int = int(line)
        #check each integers
        #if even
        if num_in_int % 2 == 0:
            print(str(num_in_int))
            # get the square of the integer
            # append to double.txt
        #if odd
            # get the cube of the integer
            # append to triple.txt
