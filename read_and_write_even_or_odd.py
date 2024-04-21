# pseudocode:
#    create numbers.txt file
#    write 20 integers in the txt file
#    open txt file
#    read txt file per line
#        strip "\n"
#        convert str to int
#        test if int is even or odd
#        if even, append to string of even numbers
#        if odd, append to string of odd numbers
#    change color of both string
#    append list of even numbers to even.txt
#    append list of even numbers to even.txt
#    close txt file
#    if possible, make things fancy

even_numbers = ""
odd_numbers = ""
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        line = line.rstrip("\n")
        line = int(line)
        if line % 2 == 0: #checks if int is even
            even_numbers = even_numbers + ", " + str(line)
        else: #checks if int is odd
            odd_numbers = odd_numbers + ", " + str(line)
even_numbers = "LIST OF EVEN NUMBERS: " + even_numbers.lstrip(", ")
odd_numbers = "LIST OF ODD NUMBERS: " + odd_numbers.lstrip(", ")
