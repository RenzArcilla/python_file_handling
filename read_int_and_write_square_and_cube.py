# pseudocode:
#     create input file, add 20 ints
#     open txt output file for squared ints
#         write a string for label
#     open txt output file for cubed ints
#         write a string for label
#     open input file and read line by line
#         store line as str in a variable
#         remove unnecessary characters
#         convert str to int
#         compute for square and store in a variable
#         compute for cube and store in a variable
#         use string formatting to store both input and output (square) in a variable
#         use string formatting to store both input and output (cube) in a variable
#         open txt output file for squared ints
#             write the string containing both input and output (square)
#         open txt output file for cubed ints
#             write the string containing both input and output (cube)


#     open txt output file for squared ints
with open("double.txt", "a") as output_file_for_squares:
    #         write a string for label
    output_file_for_squares.write("INPUT: SQUARED")
    output_file_for_squares.write("\n")

#     open txt output file for cubed ints
with open("triple.txt", "a") as output_file_for_squares:
    #         write a string for label
    output_file_for_squares.write("INPUT: CUBED")
    output_file_for_squares.write("\n")