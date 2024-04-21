from tkinter import *
# pseudocode:
#     create a window
#     display instructions as text on window
#     create an entry widget in window for users to enter statements
#     create button for user to submit their statement
#     append the submitted statement on a txt file
#     create an exit button that exits window and terminates the program
#     make things fancy(resize, change bg and fg colors)

#creates a window
window = Tk()
window.geometry("900x300")
window.resizable(False, False)
window.config(bg="BLACK")

#     display instructions as text on window
instructions = Label(window, text="Please input a statement on the text box." + "\n" + "Click 'ENTER' to submit a statement." + "\n" + "Click 'EXIT' to close the program.", font=("Times New Roman", 20, "bold"))
instructions.config(bg="BLACK", fg="WHITE")
instructions.pack()

#     create an entry widget in window for users to enter statements
statement_input_widget = Entry()
statement_input_widget.config(width=25)
statement_input_widget.config(font=("Times New Roman", 40))
statement_input_widget.config(bg="GRAY", fg="WHITE")
statement_input_widget.pack()

#     append the submitted statement on a txt file
def submit():
    user_statement = statement_input_widget.get() # stores the current text in the widget to the variable
    with open("mylife.txt", "a") as output_file: # opens file, permission set to append
        output_file.write(user_statement)
        output_file.write("\n")

#     create button for user to submit their statement
submit_button = Button(text="SUBMIT", font=("MS Serif", 20, "bold"), command=submit) # submit() is a function, the function is called when button is clicked
submit_button.config(bg="CYAN", fg="WHITE")
submit_button.pack()

#     create an exit button that exits window and terminates the program
exit_button = Button(text="EXIT", font=("MS Serif", 20, "bold"), command=quit) # the window is terminated when exit button is clicked
exit_button.config(bg="RED", fg="WHITE")
exit_button.pack()

window.mainloop()