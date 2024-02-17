import requests





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
