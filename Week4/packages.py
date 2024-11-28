# import cowsay

# name = "Abdul Rehman".lower()

# if name == "abdul rehman":
#     # cowsay.cow("Hello, " + name)
#     cowsay.trex("Hello, " + name)

# ---------------------------------------------------------------------------------
# i-tunes --------------------------
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
# print(json.dumps(response.json(), indent=2))