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

with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        line = line.rstrip("\n")
        line = int(line)
        if line % 2 == 0: #checks if int is even
            pass
#            with open("even.txt", "a") as even_numbers_file:
#                even_numbers_file.write(str(line))
#                even_numbers_file.write("\n")
        else: #checks if int is odd
            pass
#            with open("odd.txt", "a") as odd_numbers_file:
#                odd_numbers_file.write(str(line))
#                odd_numbers_file.write("\n")