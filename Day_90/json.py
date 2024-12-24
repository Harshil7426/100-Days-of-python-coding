import requests, json 
for i in range(0,10):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code == 200:
    user = result.json()
    for person in user["results"]:
      filename = f"""{person["name"]["first"].lower()} {person["name"]["last"].lower()}.jpg"""
      
      picture = requests.get(person["picture"]["medium"])
      f = open(filename, "wb")
      f.write(picture.content)
      f.close()
      print(f"Saved {filename}")