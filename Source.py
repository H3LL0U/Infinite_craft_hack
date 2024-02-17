import requests
import requests_html
from nltk.corpus import wordnet
import nltk
from typing import Generator
from tkinter_widgets import *
import tkinter as tk

def get_nouns(Word_count = 0) -> Generator[str, None, None]: 
        
    
        
        for synset in wordnet.all_synsets(pos=wordnet.NOUN):
            for lemma in synset.lemmas():
                noun_name = lemma.name().replace("_", " ") 
                yield noun_name + " "
                
                Word_count-=1
                if Word_count<=0:
                    return
                    
                    
def words_to_items(words: list) -> str:
    
    main_words = ["Water ", "Fire ", "Wind ", "Earth "]
    items = [f'{{"text":"{word[:-1]}","emoji":"{word[-1]}","discovered":false}}' for word in main_words]
    items += [f'{{"text": "{word[:-1]}","emoji":"{word[-1]}"}}' for word in words]
    return f'{{"elements":{items}}}'.replace("'", "")


    

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