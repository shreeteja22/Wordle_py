import random

def rules():
    print("\n")
    print("The rules are simple: ")
    print("A. You have to guess a 5-letter word.")
    print("B. You have 6 chances to guess the word.")
    print("C. After each guess, you will be given hints.")
    print("D. The hints are: ")
    print("🟨 - Letter is present in the word but at a different position.")
    print("🟩 - Letter is present in the word and at the correct position.")
    print("🟥 - Letter is not present in the word.")
    print("E. You can only guess a 5-letter word.")
    print("F. You can only guess a word once.")
    print("\n")

def words_picking(allow_words):
    return random.choice(allow_words)

def guess_work(allow_words):
    while True:
        guess = input("Enter a 5-letter word: ").lower()
        if len(guess) != 5:
            print("Word must be exactly 5 letters. Try again.")
        elif guess not in allow_words:
            print("Invalid word! Please enter a valid guess.")
        else:
            return guess

def results_show(target_word, guess):
    note = []
    emojis = []

    for i in range(5):
        if guess[i] == target_word[i]:
            note.append(guess[i])
            emojis.append("🟩")
        elif guess[i] in target_word:
            note.append(guess[i])
            emojis.append("🟨")
        else:
            note.append(guess[i])
            emojis.append("🟥")
    
    print("   ".join(note))
    print("  ".join(emojis))

def main():
    path = "words.txt"
    try:
        with open(path, "r") as file:
            allow_words = file.read().splitlines()
    except FileNotFoundError:
        print("Error: words.txt not found.")
        return

    while True:
        print("\nWelcome to the Daily Wordle Quiz! 🎯\n")
        print("Enter 1 - For Rules")
        print("Enter 2 - For Playing The Game")
        print("Enter 3 - To Quit The Game\n")

        try:
            choice = int(input("Enter Number (1/2/3): "))
        except ValueError:
            print("\nInvalid input! Please enter 1, 2, or 3.")
            continue

        if choice == 1:
            rules()
        elif choice == 2:
            print("\nWelcome To The Game Of WORDLE!")
            target_word = words_picking(allow_words)
            # print(target_word) #execute just to debug the code and check the target word
            for attempt in range(1, 7):
                guess = guess_work(allow_words)
                results_show(target_word, guess)
                
                if guess == target_word:
                    print(f"\nCongrats! You Guessed The Word In {attempt} Attempt(s)! 🎉\n")
                    print("----------------------------------------------")
                    break
            else:
                print(f"\nSorry! The Correct Word Was {target_word}.\n")

            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print("\nUntil We Meet Again... Quitting...")
                break
        elif choice == 3:
            print("\nUntil We Meet Again... Quitting...")
            break
        else:
            print("\nEnter A Valid Number - (1/2/3).....Try Again!")
            print("----------------------------------------------")

main()



#gonna add daily word using api in a week or future ....stay tuned for that 

# import datetime

# def guess_today_word():
#     today = datetime.datetime.now()
#     return today