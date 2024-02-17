import requests




s = requests.Session()
def combine_two(first, second):
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
        "_ga": input("enter _ga cookie:\n"),
        "_ga_L7MJCSDHKV": "enter _ga_L7MJCSDHKV cookie:\n"
    },
    auth=(),
)


    return((request.text))
print(combine_two("LALA", "LALA"))