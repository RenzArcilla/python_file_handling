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

#     display instructions as text on window
instructions = Label(window, text="Please input a statement on the text box." + "\n" + "Click 'ENTER' to submit a statement." + "\n" + "Click 'EXIT' to close the program.")
instructions.pack()

window.mainloop()