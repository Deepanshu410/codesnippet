'''1 
print(__name__) # returns script2 if imported and ran into script1, which means within script2 __name__ is a variable containing value scipt2
'''

'''2
from script1 import * #vice verca of 1
print(__name__)
'''
#3
from script1 import *
def drink(derinkh):
    print(f"Your drink {derinkh}")

def main():
    print("This is script2")
    food("cURD")
    drink("Buttermilk with black salt")
    print("This is script2 again")

if __name__ == "__main__":
    main()
