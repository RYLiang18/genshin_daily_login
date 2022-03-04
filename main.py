import requests, json, os, time, random, pprint

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
mhy_uuid=os.eviron.get("mhy_uuid")

url = "https://hk4e-api-os.mihoyo.com/event/sol/sign?lang=en-us"

payload = f"{{\"act_id\": \"{act_id}\"}}"

header = {
    "Cookie": f"_MHYUUID={mhy_uuid}",
    "User-Agent": user_agent,
    "Origin": origin,
    "Referer": referer
}


# wait random time of 1 - 3600 seconds

print("============= bot start =============")

res = requests.post(
    url,
    data = payload,
    headers = header
)

res_json = res.json()

print("Bot Results...")
pp.pprint(res_json)