try:
    value = input("Enter number: ")
    num = int(value)
    print(num)
except:
    print("Invalid input")

data = input("Enter name: ")
if data.strip() == "":
    print("Empty input not allowed")
else:
    print(data)
