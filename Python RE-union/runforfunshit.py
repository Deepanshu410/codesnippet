'''# HANGMAN GAME
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

if __name__== "__main__":
    main()'''


