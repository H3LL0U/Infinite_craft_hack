import requests
import requests
import requests_html
from nltk.corpus import wordnet
import nltk
from typing import Generator

def get_nouns(Word_count = 0) -> Generator[str, None, None]: 
        '''
        Word_count = how many words to generate up to 146347

        output: A list of random nouns with a space at the end(see words_to_items() function). (they are going to still be the same on each function call)

        if the value is set under 0 returns a list of 146347 words



        ''' 
    
        
        for synset in wordnet.all_synsets(pos=wordnet.NOUN):
            for lemma in synset.lemmas():
                noun_name = lemma.name().replace("_", " ") 
                yield noun_name + " "
                
                Word_count-=1
                if Word_count==0:
                    return
                    
             
def words_to_items(words: list) -> str:
    '''
    Takes in a list of words and returns a json string that can be put in local storage at the https://neal.fun/infinite-craft/ website
    the ending character of the word is interpreted as an emoji and is not going to appear in the string
    Words Water, Fire, Wind and Earth are automatically added
    '''
    main_words = ["Water ", "Fire ", "Wind ", "Earth "]
    items = [f'{{"text":"{word[:-1]}","emoji":"{word[-1]}","discovered":false}}' for word in main_words]
    items += [f'{{"text": "{word[:-1]}","emoji":"{word[-1]}"}}' for word in words]
    return f'{{"elements":{items}}}'.replace("'", "")


def combine_two(first: str, second: str, cookie1: str, cookie2: str, s = requests.Session)->str:
    '''
    first = a word that you want to combine
    second = another word you want to combine
    cookie1 = a cookie _ga from your browser
    cookie2 = a cookie _ga_L7MJCSDHKV from your browser
    s = session of the request (can remain as it is)
    output --> a response from the server
    '''
    request = s.get(f"https://neal.fun/api/infinite-craft/pair?first={first}&second={second}",
    headers={
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,nl;q=0.6",
        "authority": "neal.fun",
        "referer": "https://neal.fun/infinite-craft/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    },
    cookies={
        "_ga": cookie1,
        "_ga_L7MJCSDHKV": cookie2
    },
    auth=(),
)


    return((request.text))
