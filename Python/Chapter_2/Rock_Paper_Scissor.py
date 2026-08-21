import random
def game (c,d): 
    if c == d:
        return None
    if c == "Rock":
        if d == "Paper":
            return True
        elif d == "Scissor":
            return False
    elif c == "Paper":
        if d == "Scissor":
            return True
        elif d == "Rock":
            return False
    elif c == "Scissor":
        if d == "Rock":
            return True
        elif d == "Paper":
            return False


rand = random.randint(1,3)
print("COMPUTER'S TURN: Rock , Paper , or Scissor\n ")
if rand == 1:
    comp = "Rock"
elif rand == 2:
    comp = "Paper"
elif rand == 3:
    comp = "Scissor"

You = input("YOUR TURN: Rock ,Paper , Scissor\n ")

print(f"Computer Choose :- {comp}")
print(f"YOU Choose :-  {You}")

f = game(comp,You)

if f == None:
    print("tie")
elif f == True :
    print("you win")
elif f == False :
    print("YOu lose")