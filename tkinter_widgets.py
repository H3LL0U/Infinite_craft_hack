from typing import Tuple
from customtkinter import *
import tkinter as tk
from tkinter import messagebox
from functions import *

class window(CTk):
    '''
    Initial Window
    '''
    def __init__(self, geo=None, mode="System", title="Infinite craft hack") -> None:
        super().__init__()
        if geo != None:
            self.geometry(geo) 
        set_appearance_mode(mode)
        self.title(title)

    def change_geo(self, new_geo):
        self.geometry(new_geo)

class Number_Of_Words_Selector(CTkScrollableFrame):
    '''
    An area where you can select how many extra words to add to your json
    '''
    def __init__(self, master, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(master,**kwargs)

        self.frame = CTkFrame(master=master)
        self.frame.pack()
        self.label = CTkLabel(master=self.frame,text="Please select how many nouns you want to add:")
        self.label.pack(pady = 10, padx = 10)


        self.entry_grid = CTkFrame(self.frame)
        self.entry_grid.pack(pady = 10, padx = 10)
        self.entryVar = StringVar()
        self.entry = CTkEntry(master=self.entry_grid,textvariable=self.entryVar)
        self.entry.grid(column = 1, row = 1, padx = 5)

        self.emoji_entry_Var = StringVar()
        self.emoji_entry = CTkEntry(self.entry_grid,28, textvariable=self.emoji_entry_Var)
        self.emoji_entry.grid(column = 2,row = 1, padx = 5)

        self.emoji_label = CTkLabel(self.entry_grid,text="Emoji")
        self.emoji_label.grid(column= 3,row = 1, padx = 5)
        self.emoji_entry_Var.trace_add('write',self.callback_emoji)

        #Check if the number has been entred
        self.entryVar.trace_add("write", lambda *args: callback(self,self.entryVar.get()[-1]) if len(self.entryVar.get()) !=0 else None)
        def callback(self, added_symbol):
            try:
                int(added_symbol)
                if int(self.entryVar.get()) > 7000:
                    raise(Exception("too big"))
            except:
                self.entryVar.set(self.entryVar.get()[:-1])

        
        self.button = CTkButton(self.frame, text= "Confirm", command= self.button_command)
        self.button.pack( pady = 10, padx = 10)

    def callback_emoji(self, *args):
        
        if len(self.emoji_entry_Var.get())>1:
            self.emoji_entry_Var.set(self.emoji_entry_Var.get()[:1])
    def button_command(self):
        try:
            nouns_count = int(self.entryVar.get())
            with open("generated code.txt",'w',encoding="UTF-8") as file:
                file.write(generate_script(words_to_items(list(get_nouns(nouns_count,self.emoji_entry_Var.get())))))
            messagebox.showinfo("Completed!", "The generation completed successfully! (Check generated code.txt)")
        except Exception as error:
            messagebox.showerror("An error acured!", str(error))
            raise(error)



                
                

        

    



        




    


        

        

