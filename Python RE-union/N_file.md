## File Detection



**for file detection we can use either relative or absolute paths;**

\# Relative = folder/text.txt, Absolute = C:/Users/file/test.txt



1. ###### **To check if a file path exists, and whether it's folder/directory or file.**

&#x09;import os

&#x09;**# Normally, a Python script only interacts with its own variables and memory. Importing the os module allows your program to "step outside" of itself and perform system-level 	tasks. It bridges the gap by acting as a universal translator, so you don't have to write different code for Windows and Mac.**

&#x09;file\_path = "text.txt"

&#x09;if os.path.exists(file\_path):

&#x20;   		print(f"Location '{file\_path}' exists")

&#x20;   		if os.path.isfile(file\_path):

&#x20;       		print("It's a file and not a folder")

&#x20;   		elif os.path.isdir(file\_path):

&#x20;       		print("It's a directory/folder and not a file")

&#x09;else:

&#x20;   		print("Location doesn't exist")'''





###### **# Writing \& Appending files (.txt, .json(made of keyvalue pairs), .csv(comma separated value))**

txt\_data = "what in the world"

file\_path1 = "output.txt"

'''with open(file\_path1, "w") as file: # **with** is a statement, used to wrap a block of code to execute, if we open a file the with statement will also close that file when we're done with     it. The **open** function returns a file object. as file, file here is the name of the file object.

&#x20;   # the second parameter is the mode, **"w"** is for write **"x"** also writes if the file doesn't exist if it does exit there'll be an error, **"a"** is to append a file, **"r"** is for read

&#x20;   pass'''



###### **# TXT**

\#with open(file\_path1, "w")as file:

\#    file.write(txt\_data)

\#    print(f"text file '{file\_path1}' created")

\#try:

\#    with open(file\_path1, "x")as file:

\#        file.write(txt\_data)

\#        print(f"text file '{file\_path1}' created")

\#except FileExistsError:

\#    print("file already exits")

\#try:

\#    with open(file\_path1, "a")as file:

\#        file.write("\\n" + txt\_data)

\#        print(f"text file '{file\_path1}' created")

\#except FileExistsError:

\#    print("file already exits")



###### **#JSON**

import json

employee2 = {

&#x20;   "name" : "Spongebob",

&#x20;   "age" : 20,

&#x20;   "job" : "Cook"

}

file\_path2 = "output2.json"

\#try:

\#    with open(file\_path2, "w")as file:

\#        json.dump(employee, file, indent=4) #json.dump() changes the dictionary to string

\#        print(f"json file '{file\_path2}' created")

\#except FileExistsError:

\#    print("file already exits")



###### **#CSV**

import csv

employee3 = \[\["Name", "Age", "Job"],\["sony", 20, "cook"],\["mony", 30, "unemployed"],\["tony", 40, "businessman"]]

file\_path3 = "output3.csv"

\#try:

\#    with open(file\_path3, "w", **newline=""**)as file:

\#        writer = csv.writer(file) # writer is an object, it provides methods for providing data to a csv file

\#        for row in employee3:

\#            **writer.writerow(row)**

\#        print(f"csv file '{file\_path3}' created")

\#except FileExistsError:

\#    print("file already exits")





###### **# READING FILES(.txt, .json, .csv)**

###### **# TXT**

\#try:

\#    file\_path4 = "output.txt"

\#    with  open(file\_path4, "r") as file:

\#        content = file.read()

\#        print(content)

\#except PermissionError:

\#    print("permission to this file is limited")

###### **#JSON**

\#try:

\#    file\_path4 = "output2.json"

\#    with  open(file\_path4, "r") as file:

\#        content = json.load(file)

\#        print(content\["name"]) #can access the value by its key

\#except PermissionError:

\#    print("permission to this file is limited")

###### **#CVS**

\#try:

\#    file\_path4 = "output3.csv"

\#    with  open(file\_path4, "r") as file:

\#        content = **csv.reader(file)** # gives memory address, to access the data we need to iterate the data line by line

\#        for line in content:

\#            print(line\[0]) #can access lines of data through index

\#except PermissionError:

\#    print("permission to this file is limited")

