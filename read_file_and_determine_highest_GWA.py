# pseudocode:
#    create input file and write 20 values of names and GWAs
#    open input file
#    read input file, line by line
#        split name and GWA values
#        assign name to a variable
#        assign GWA to a variable
#        convert str to float
#        check if the GWA is higher than the current highest GWA
#        if true:
#            assign GWA value as the new current highest GWA
#            assign name value as name of current highest GWA
#        else:
#            current highest GWA and name stays the same
#    create window
#    in window, display highest GWA and name of student who got highest GWA

current_highest_gwa = 0.00 #initializes current_highest_gwa
with open("name_and_gwa.txt", "r") as name_and_gwa_file:
    for line in name_and_gwa_file:
        name_and_gwa = line.rstrip('\n')
        name_and_gwa = name_and_gwa.split(":")
        name = name_and_gwa[0]
        gwa = name_and_gwa[1]
        print(name, gwa)