# FOR while loops, and if/else statements. A command-line program where you type in an expense category and amount, saving them to a python list or dictionary. 
# user prompt, organise the prompt(loop, statements), save it to a dict. 

c = 3
dict = {}
while True:
    key = input("Enter Expense: ")
    item = input("Enter Amount: ")
    dict.update({key:item})
    c -= 1
    print(dict)
    if c == 0:
        print("Entry full")
        break

print(dict)

# Save the above dictionary to a file (.csv, .json)

file_path = "first/output.csv"
try: 
    with open(file_path, "a", newline="")as file:
        file.write(str(dict))
        print(f"text file '{file_path}' created")
except FileExistsError:
    print("file already exits")