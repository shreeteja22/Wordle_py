import random

def rules():
    print("The rules are simple: ")
    print("A. You have to guess a 5 letter word.")
    print("B. You have 6 chances to guess the word.")
    print("C. After each guess, you will be given hints.")
    print("D. The hints are: ")
    print("🟨- Letter is present in the word but at a different position.")
    print("🟩- Letter is present in the word and at the correct position.")
    print("🟥- Letter is not present in the word.")
    print("E. You can only guess a 5 letter word.")
    print("F. You can only guess a word once.")

def words_picking(allow_words):
    target_word = random.choice(allow_words)
    return target_word

def guess_work(allow_words):
    while True:
        guess = input("Enter the 5 letter word: ").lower()
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
    print("1 - For Rules")
    print("2 - For Playing The Game")
    print("3 - To Quit The Game")
    choice = int(input("Enter Number (1/2/3): "))

    path = "words.txt"
    with open(path, "r") as file:
        allow_words = file.read().splitlines()

    while True:
        if choice == 1:
            rules()
            break
        elif choice == 2:
            print("Welcome To The Game Of WORDLE!")
            target_word = words_picking(allow_words)
            for attempt in range(1, 7):
                guess = guess_work(allow_words)
                if guess == target_word:
                    print(f"Congrats! You Guessed The Word In {attempt} Attempt(s)! 🎉")
                    break
                results_show(target_word, guess)
            else:
                print(f"Sorry! The Correct Word Was {target_word}.")
                break
        elif choice == 3:
            print("Until We Meet Again... Quitting...")
            break
        else:
            print("Enter A Valid Number - (1/2/3) ")

main()
