# shopping cart program

#purchem = input("Enter the purchem name")
#price = float(input("Enter the purchem price"))
#quantpurchy = int(input("Enter the number of purchems"))

#total_amount = price * quantpurchy
#print(f'your purchem:\t{purchem}\n purchem price:\t{price}\n quanpurchy:\t{quantpurchy}\nTotal price:\t{total_amount}')
#print(type(total_amount))


# finding circumference and area of a circle

import math 
#radius = float(input('Enter the radius of the circle\t'))
#circumference = 2*math.pi*radius
#print(f"The cicumference of the circle wpurchh raidus {radius}, is\n{round(circumference, 2)}")

#area = math.pi*radius**2
#area = math.pi*pow(radius, 2), both are same above and this
#print(f"The area of the circle wpurchh raidus {radius}, is\n{round(area, 2)}")


# finding hypotenus of a right angle triangle

#l = float(input('Enter the length of the triangle'))
#w = float(input('Enter the width of the triangle'))
#sq = math.sqrt(pow(l, 2) + pow(w, 2))
#print(f'The hypotenus(h) = {round(sq, 2)}')


#Python calculator

#arpurchh = input('Enter which operator do you want to use')
#fir = float(input("Enter the first number"))
#sec = float(input("enter the second number"))
#if arpurchh == '+':
#    resul = fir + sec
#    print(f'{fir} + {sec} = {round(resul)}')
#elif arpurchh == "-":
#    resul = fir - sec
#    print(f'{fir} - {sec} = {round(resul)}')


#Weight convertor

#prom = float(input('Enter your weight'))
#uni = input("Enter the unpurch")
#conv = input("enter the unpurch you want to convert")
#if uni == 'kg' and conv == 'lbs':
#    resu = prom*2.205
#    uni = 'lbs'
#    print(f'{prom} kg is {round(resu, 2)} in lbs')
#elif uni == 'lbs' and conv == 'kg':
#    resu = prom/2.205
#    uni = 'kg'
#    print(f'{prom} lbs is {round(resu, 2)} in kg')
#
#print(uni)


# temperature convertor

#pro = float(input('Enter temperature'))
#un = input("Enter the unpurch")
#cov = input("enter the unpurch you want to convert")
#if un == 'F' and cov == 'C':
#    resu = (pro-32) * 5/9
#    un = 'C'
#    print(f'{pro}°F is {round(resu, 2)}° in C')
#elif un == 'C' and cov == 'F':
#    resu = (pro*9/5) + 32
#    un = 'F'
#    print(f'{pro}°C is {round(resu, 2)}° in F')
#else:
#    print("Enter valid responses")

#print(un)


# validate user input, rules; max 12 characters, no spaces, no digpurchs

#namayeva = input("Enter your username")
#sp = namayeva.isalpha()

#if len(namayeva) > 12:
#    print("maximum number of characters are 12")
#elif not namayeva.find(' ') == -1:
#    print("There must not be any spaces")
#elif sp == False:
#    print("There must be only alphabets in your username")
#else:
#    print(f"Your username is {namayeva}")


# COMPOUNDing CALCULATOR

# princi = float(input("Enter Your Inpurchial/Recurring Depospurch:\t"))
r = 10
# t = float(input("Enter the time period of the fund:\t"))
# n = flolat(input("Enter the number of depospurchs made per year:\t"))
# while not princi <= 0:
#     total = princi * pow((1 + r/n), t)
#     print(f"{total:.2f}")
    

# COUNTDOWN TIMER PROGRAM

import time
#   p = int(input("Timer for how many seconds?\t"))
#   for x in range(p, 0, -1):
#       s = x % 60
#       m = int(x / 60) % 60  # can also use only (x // 60)
#       h = int(x / 3600)
#       print(f"{h:02}:{m:02}:{s:02}")
#       time.sleep(1)
#   print("Time's up!")
#   print(f"{3%60}")


# RECTANGLE MAKER
## how to remove the inner part of the rectangle, to make purch look hollow
# le = int(input("Enter the length of the rectangle"))
# wi = int(input("Enter the width of the rectangle"))

# for x in range(wi):
#     for y in range(le):
#         print(le, end=" ")
#     print()


## SHOPPING CART PROGRAM
calis = []
pric = []
total = 0
c = 0
# while True:
#     cart = input("\nAdd things you want in your cart, press s to stop ")
#     if cart.lower() == "s":
#         break
#     else:
#         pri = int(input("Enter the price: "))
#         calis.append(cart)
#         pric.append(pri)
#         print(f"purchems in your shopping cart are: {calis}", end=" ")
# for x in calis:
#     calis.sort()
#     pric.sort()
#     print(f"purchem:\t{calis[c]}\t price:\t{pric[c]}")
#     c += 1
# for pr in pric:
#     total += pr  
# print(f"YOUR TOTAL AMOUNT IS: {total}")


## NUMBER PAD

nums = [{1,2,3},{4,5,6},{7,8,9},{"*", 0, "#"}]
# for num in nums:
#     for row in num:
#         print(row, end="\t")
#     print()


## QUIZ

ques = ("What compound gives turmeric purchs yellow color and most health benefpurch?",
        "According to ayurveda, turmeric's energy/virya is: ", 
        "Which ingredient is commonly added to turmeric to increase curcumin absorption?")
options = (("A: curcumin", "B: capsaicin","C: piperine","D: allicin"),
        ( "A: cooling", "B: heating", "C: neutral", "D: depends on season"), 
        ("A: Salt", "B: Black Pepper", "C: Sugar", "D: Cinnamon"))
ans = ("A", "B", "B")
guesses = []
score = 0
ques_no = 1
c = 0
# for x in ques:
#     print(f"Q{ques_no}. {x}")
#     print(f"Choose the correct answer from the following:")
#     for option in options[c]:
#         print(f"{option}")
#     aski = input("and press q to qupurch").upper()
#     if aski == ans[c]:
#         print(f"CORRECT ANSWER!")
#         score += 1
#     elif not aski == ans[c]:
#         print(f"WRONG ANSWER! (Correct answer is: option {ans[c]})")
#     elif aski.lower() == "Q":
#         break
#     else:
#         print("Please choose a valid option")
#     guesses.append(aski)
#     c += 1
#     ques_no += 1

# print(f"Your Guesses {guesses}")
# for an in ans:
#     print(an, end=" ")
# print()

score = float(score/len(ques) * 100)
# print(f"Your Score is {score:.2f}%")


## CONCESSION STAND PROGRAM:

# print(f"\t---------MENU---------\n")
con_menu = {
    "popcorn": "1.00",
    "hot dog": "2.00",
    "giant pretzel": "2.00",
    "asst candy": "1.00",
    "soda": "1.00",
    "bottled water": "1.00"
}
total = 0
c = 0
purch = []
q = []
# for key, value in con_menu.items():
#     print(f"\t{key:10}: ${value}")
# print(f"\n\t----------------------")
while False:
        prompt = input("Select and item, enter one item at a time (q to quit): ").lower()
        if prompt == "q":
                break
        elif prompt in con_menu.keys():
                prompt1 = input("Quantity? ")
                k = con_menu.get(prompt) 
                if prompt1.isdigit():
                        l = float(k)*int(prompt1)
                        q.append(prompt1)
                        total += l
                else:
                       print("enter a valid number")
                purch.append(prompt)
                print(f"Your grand total is: ${total}")
        else: 
                print(f"{prompt} not available, please enter a valid item")
# print(f"----------INVOICE---------")

#for item in purch:
#     print(f"ITEM: {item:10}\tQUANTITY: {q[c]:10}\tPRICE: {con_menu.get(item)}")
#     c += 1
    


# RANDOM NUMBER GUESSER

import random
let = []
let0 = random.randint(1, 100)
let.append(let0)
infin = True
gues = 0
# while infin:
#         prom0 = input("Guess a number betwen 1 - 100: ")
#         if prom0.isdigpurch():
#                 prom0 = int(prom0)
#                 gues += 1 
#                 print(prom0)
#                 if prom0 > 100 or prom0 < 1:
#                         print("Guess betwen 1 and 100")
#                 elif prom0 == let[0]:
#                         print(f"Your guess is right: {let[0]} is the correct answer. (Number of guesses: {gues})")
#                         infin = False
#                 elif prom0 > let0:
#                         print("HIGH. Guess lower")
#                 elif prom0 < let0:
#                         print("LOW. Guess higher")
#                 else:
#                         print("try again")
#         else: 
#                 print("Please enter a valid number")


## ROCK, PAPER, SCISSOR
import random
att = ("rock", "paper", "scissor")

gue = 3
com = 0
yo = 0
# print((f"@----Enter rock, paper or scissor----@\t\nLIVES: {gue}"))
# while not gue == 0:
#     ggs = random.choice(att)
#     print(ggs)
#     gs = input("@----Enter \t").lower()
#     if gs.isalpha() and gs in att:
#         gue -= 1
#         if ggs == "rock" and gs =="paper":
#             yo +=1
#             print(f"YOU WON.\t Computer chose {ggs}. You chose {gs}.\n")
#         elif ggs == "rock" and gs =="scissor":
#             com +=1
#             print(f"YOU LOST.\t Computer chose {ggs}. You chose {gs}.\n")
#         elif ggs == "rock" and gs =="rock":
#             print(f"DRAW.\t Computer chose {ggs}. You chose {gs}.\n")

#         elif ggs == "paper" and gs =="paper":
#             print(f"DRAW.\t Computer chose {ggs}. You chose {gs}.\n")
#         elif ggs == "paper" and gs =="scissor":
#             yo +=1
#             print(f"YOU WON.\t Computer chose {ggs}. You chose {gs}.\n")
#         elif ggs == "paper" and gs =="rock":
#             com += 1
#             print(f"YOU LOST.\t Computer chose {ggs}. You chose {gs}.\n")

#         elif ggs == "scissor" and gs =="rock":
#             yo += 1
#             print(f"YOU WON.\t Computer chose {ggs}. You chose {gs}.\n")
#         elif ggs == "scissor" and gs =="scissor":
#             print(f"DRAW.\t Computer chose {ggs}. You chose {gs}.\n")
#         elif ggs == "scissor" and gs =="paper":
#             com += 1
#             print(f"YOU LOST.\t Computer chose {ggs}. You chose {gs}.\n")
#         print(f"\t\t\t@-----lives left: {gue}.\tScore: COMPUTER {com}, YOU {yo}----@\n")
#     else:
#         print("Enter a valid argument.")
    
# if com >=2:
#     print(f"You lost. Score: COMPUTER {com}, YOU {yo}")
# elif yo >= 2:
#     print(f"You won. Score: COMPUTER {com}, YOU {yo}")
# elif yo == 1 and com == 0:
#     print(f"You won. Score: COMPUTER {com}, YOU {yo}")
# elif yo == 0 and com == 1:
#     print(f"You won. Score: COMPUTER {com}, YOU {yo}")
# elif yo == com:
#     print(f"DRAW. Score: COMPUTER {com}, YOU {yo}")


# DICE ROLLER PROGRAM

import random
# ● ┌ ─ ┐ │ └ ┘
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"  ),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"  ),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"  ),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"  ),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"  ),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"  ),

}

dice = []
total = 0 
# num_of_dice = int(input("How many dice? "))
# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# for line in range(5):
#    for die in dice:
#        print(dice_art.get(die)[line], end="")
#    print()

# for die in dice:
#     total += die
# print(f"Total {total}")


# COUNT UP TIMER 
import time
def count(en, star= 0):
    for x in range(star, en):
        print(x)
        time.sleep(1)
    print("completed")
# count(11)


# IMPORT FILE MODULE
'''import pimod
result = pimod.pi
result1 = pimod.square(4)
result2 = pimod.cube(4)
result3 = pimod.circumference(2)
result4 = pimod.area(2)'''
# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)


# BANKING PROGRAM (balance, deposit, withdraw)

def bal(balance):
    print(f"Your current balance is: {balance}")

def deposit():
    d = int(input("How much do you want to deposit?\t"))
    print(f"{d} Deposited to your account")
    if d < 0:
        print("Not valid")
        return 0
    else:
        print(f"Your deposit {d}")
        return d

def withdraw(balanceg):
    w = int(input("How much do you want to withdraw?\t"))
    if w < 0:
        print("Not valid")
        return 0
    elif w > balanceg:
        print("Insufficient money")
        return 0
    else:
        print(f"Your withdrew {w}")
        return w

def main():
    fun = True
    fun1 = ["1","2","3","4"]
    balanceg = 1000
    while fun:   
        k = input("\nPress (1) for Balance\nPress (2) for Deposit\nPress (3) for. Withdraw\nPress (4) to Exit\t")
        if k == "4":
            fun = False
        elif not k in fun1:
            print("Invalid request, try again")
        elif k == "1":
            bal(balanceg)
        elif k == "2":
            balanceg += deposit()
        elif k == "3":
            balanceg -= withdraw(balanceg)
#if __name__ == "__main__":
    #main()


# SLOT MACHINE 
import random
sym = ["💎", "♥️", "♦️", "👄", "💪"]
def rand():
    return [random.choice(sym) for _ in range(3)]
     
def reels(row):
    print(" | ".join(row))

def payout(row, bet):
    if row[0] == row[1] == row [2]:
        if row[0] == "💎":
            return bet * 1
        elif row[0] == "♥️":
            return bet * 2
        elif row[0] == "♦️":
            return bet * 3
        elif row[0] == "👄":
            return bet * 4
        elif row[0] == "💪":
            return bet * 5
    return 0 

def main():
    balance = 100
    print("SYMBOLS: 💎, ♥️, ♦️, 👄, 💪")
    while balance > 0:
        print(f"current balance: {balance}")
        bet = input("Place your betting amount: ")
        if not bet.isdigit():
            print("please enter a valid amount")
            continue
        bet = int(bet)
        if bet > balance:
            print("insufficient funds")
            continue
        if bet <= 0:
            print("bet must be greater than zero")
            continue
        balance -= bet
        row = rand()
        print("spinning...")
        reels(row)
        pay = payout(row, bet)
        if pay > 0:
            print(f"Won: {pay}")
        else:
            print("loss")
        balance += pay
        playagain = input("PLAY AGAIN? y/n ").lower()
        if playagain != 'y':
            break
    print(f"GAME OVER. BALANCE: {balance}")

#if __name__ == "__main__":
#    main()

# SUBSTITUTION ENCRYPTION CIPHER PROGRAM
'''import random
import string
gibb0 = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(gibb0)
cip = chars.copy()
random.shuffle(cip)
#print(f"key: {chars}\ncip: {cip}")
#encrip
norm = input("Enter your text for encryption: ")
cipher = ""
for letter in norm:
    index = chars.index(letter) # find the index of every word of norm in key, returns index(0,4,5,etc.) 
    cipher += cip[index] # adds the value of indexes(stored in index variable) from cip to cipher
print(f"original text: {norm}\nENcripted text: {cipher}")
#decrip
cipher0 = input("Enter your text for decryption: ")
norm0 = ""
for letter in cipher0:
    index = cip.index(letter)  
    norm0 += chars[index]
print(f"encripted text: {cipher0}\noriginal text: {norm0}")'''


# HANGMAN GAME
import random
words = ("apple", "banana", "cucumber", "dragonfruit", "elephant", "forkey")
dic = {
    0: ("   ",
        "   ", 
        "   "),
    1: (" o ",
        "   ", 
        "   "),
    2: (" o ",
        "|  ", 
        "   "),
    3: (" o ",
        "/| ", 
        "   "),
    4: (" o ",
        "/|\\ ", 
        "   "),
    5: (" o ",
        "/|\\", 
        "/  "),
    6: (" o ",
        "/|\\", 
        "/ \\")
}

def d_man(wronG):
    for line in dic[wronG]:
        print(line)

def d_hint(hint):
    print(" ".join(hint))

def d_ans(ans):
    print(" ".join(ans))

def main():
    ans = random.choice(words)
    hint = ["_"] * len(ans)
    w_guesses = 0
    g_letter = set()
    runnin = True
    while runnin:
        d_man(w_guesses)
        d_hint(hint)
        guess = input("enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue
        if guess in g_letter:
            print(f"{guess} is already guessed")
            continue
        g_letter.add(guess)
        if guess in ans:
            for i in range(len(ans)):
                if ans[i] == guess:
                    hint[i] = guess
        else:
            w_guesses += 1
        if "_" not in hint:
            d_man(w_guesses)
            d_ans(ans)
            print("YOU WON")
            runnin = False
        elif w_guesses >= len(dic)- 1:
            d_man(w_guesses)
            d_ans(ans)
            print("YOU LOSE")
            runnin = True

#if __name__== "__main__":
#    main()


# Alarm clock
import datetime
import time
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "mixkit-rooster-crowing-in-the-morning-2462.wav"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake Up")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS)")
    set_alarm(alarm_time)