# pseudocode:
#    create numbers.txt file
#    write 20 integers in the txt file
#    open txt file
#    read txt file per line
#        strip "\n"
#        convert str to int
#        test if int is even or odd
#        if even, append to even.txt
#        if odd, append to odd.txt
#    close txt file
#    if possible, make things fancy

with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        line = line.rstrip("\n")
        line = int(line)
        if line % 2 == 0:
            print("EVEN:", line)
        else:
            print("ODD:", line)