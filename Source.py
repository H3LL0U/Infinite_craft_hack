from tkinter_widgets import *
import tkinter as tk
from functions import words_to_items , get_nouns


    

if __name__ == "__main__":

    main_window = window()




    main_window.mainloop()
    
'''    while True:
        try:
            iterations = int(input("How many extra words do you want to get?\n"))
            break
        except ValueError:
            print("You did not enter an integer")
        
    words = [i for i in get_nouns(5)]
    
    with open("items.txt", "a") as file:
        file.write(words_to_items(words = words).replace("\\","'"))
        print("saved to items.txt")
'''