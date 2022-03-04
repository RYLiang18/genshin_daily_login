import requests, json

"""
Note on Bot Detection

https://www.reddit.com/r/Genshin_Impact/comments/rohk7w/quick_tutorial_for_building_your_own_hoyolab/

When writing bots, it is recommended that your requests resemble your browser as much as possible
This is to keep MiHoYo from figuring out that a bot is running and potentially banning your account 
"""

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
origin = "https://webstatic-sea.mihoyo.com"
referer = "https://webstatic-sea.mihoyo.com/"