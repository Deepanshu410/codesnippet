import csv
employee3 = [["Name", "Age", "Job"],["sony", 20, "cook"],["mony", 30, "unemployed"],["tony", 40, "businessman"]] 
file_path3 = "first/output3.csv"
try: 
    with open(file_path3, "w", newline="")as file:
        writer = csv.writer(file) # writer is an object, it provides methods for providing data to a csv file
        for row in employee3:
            writer.writerow(row)
        print(f"csv file '{file_path3}' created")
except FileExistsError:
    print("file already exits")