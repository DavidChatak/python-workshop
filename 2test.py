import json
with open("phone_book.json","r") as f:
    print(f.read())
    data=json.loads(f)
    print("json file:", data)