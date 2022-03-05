import requests, os, time, random, pprint

pp = pprint.PrettyPrinter(indent = 2)

"""
Note on Bot Detection

When writing bots, it is recommended that your requests resemble your browser as much as possible
This is to keep MiHoYo from figuring out that a bot is running and potentially banning your account 
"""

# pretend that we are a browser hehe
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
origin = "https://webstatic-sea.mihoyo.com"
referer = "https://webstatic-sea.mihoyo.com/"

act_id = os.environ.get("act_id")

# cookies
mhy_uuid = os.environ.get("mhy_uuid")
ltoken = os.environ.get("ltoken")
ltuid= os.environ.get("ltuid")

# MAIN

# sleep from 1s - 3600s
# this is to add more confusion to mhy bot detection
sleep_time = random.randint(1, 3600)
print(f"SLEEPING FOR {sleep_time} SECONDS...")
time.sleep(sleep_time)

# bot starts here
url = "https://hk4e-api-os.mihoyo.com/event/sol/sign?lang=en-us"

payload = f"{{\"act_id\": \"{act_id}\"}}"

header = {
    "Cookie": f"_MHYUUID={mhy_uuid}; mi18nLang=en-us; ltoken={ltoken}; ltuid={ltuid}",
    "User-Agent": user_agent,
    "Origin": origin,
    "Referer": referer
}
print("============= bot start =============")

with requests.Session() as res:
    res = requests.post(
        url,
        data = payload,
        headers = header
    )

    res_json = res.json()

    print("Bot Results:")
    pp.pprint(res_json)

    
print("================ fin ================")