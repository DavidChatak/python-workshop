import json
menu = """
__________________________________________
Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
__________________________________________
"""


while True:
    print(menu)
    choice=input("1/2/3/4-->")
    if choice == "1":
        with open("phone_book.json","r") as f:
            data=json.load(f)
            f.close() 
        name = input("enter the name to find his/her phone number:").lower()
        print(f"the phone number of {name}: {data.get(name,'not found')} ")
        
    elif choice == "2":
        with open("phone_book.json","r") as f:
            data=json.load(f)
        name = input("enter the name :").lower()
        number = input("enter the phone number:")
        if not data.get(name):
            data[name] = number
            with open("phone_book.json", "w") as f:
                json.dump(data,f)
                f.close()   
        else:
            print(f"{name} already exist..")
    elif choice == "3":
        with open("phone_book.json","r") as f:
            data=json.load(f)
        name = input("enter the name to be deleted:").lower()
        if data[name]:
            del data[name]
            with open("phone_book","w") as f:
                json.dump(data,f)
                f.close()
        else:
            print("no such a name, try again...")
    elif choice =="4":
        print("bye bye")
        break
