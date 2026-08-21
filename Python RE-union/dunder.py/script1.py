''' 1
from script2 import * # returns script
print(__name__) # returns __main__, which means __name__ in script1 is a variable with value __main__
'''

'''2
print(__name__) # vice versa of 1
'''

def food(foohd):
    print(f"YOUR FOOD {foohd}")

def main():
    print("THis is script1")
    food("CHilla")
    print("This is scipt1 again")

if __name__ == "__main__":
    main()
