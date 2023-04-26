# Ken Leam G. Gamboa
# BSCPE 1-5
# This program identifies the even/odd numbers from a text file,
# will get the square of each even number,
# will get the cube of each odd number,
# and will append the numbers in their respective text files.

# open integer.txt, open double.txt, open triple.txt
with open ("integer.txt", "r") as integer_file, open("double.txt", "a") as double_file, open("triple.txt", "a") as triple_file: 
    #append this text in double.txt 
    double_file.write("Squaring Even Numbers:\n")

    #for each line in nembers.txt
    for line in integer_file:
        #convert each number in the line into integers
        num_in_int = int(line)
        #check each integers
        #if even
        if num_in_int % 2 == 0:
            # get the square of the integer
            double_num = num_in_int ** 2
            # append to double.txt, ^2 means the number raised to 2
            double_file.write("\t" + str(num_in_int) + "^2 = " + str(double_num) + "\n")
        #if odd
        if num_in_int % 2 != 0:
            # get the cube of the integer
            triple_num = num_in_int ** 3
            # append to triple.txt
