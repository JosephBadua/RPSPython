import random #needed for random selection 
# Online Python - IDE, Editor, Compiler, Interpreter
#Rock Paper Scissors
tie = 0
win = 0
lose = 0

def display_options(tie, win, lose):
    user_option = input("What would you like to do?\n(A) Reset your score and play again?\n(B) Play another round?\n(C) Quit Game\n")
    if user_option.lower() == 'a':
        reset_score(tie, win, lose)
    elif user_option.lower() == 'b':
        play_game(tie, win, lose)
    elif user_option.lower() == 'c':
        print("Here's a summary of your score. Thanks for playing.\nWins: "  + str(win) + "\nLosses: " + str(lose) + "\nTies: " + str(tie))
    else:
        print("Alright funny guy! I'm outta here")

def reset_score(tie, win, lose):
    tie = win = lose = 0
    print("The scores have been resetted. Good luck have fun!")
    play_game(tie, win, lose)

def play_game(tie, win, lose):
    options = ['Rock', 'Paper', 'Scissors']
    cpu_selected = options[random.randint(0, 2)]
    answer = input("Choose one: Rock, Paper, or Scissors\n").lower().capitalize()
    
    if answer != 'Rock' and answer != 'Paper' and answer != 'Scissors':
        print("Hey! That's not one of the choices")
        display_options(tie, win, lose)
    elif answer == 'Rock':
        if cpu_selected == 'Rock':
            print('The CPU selected Rock too! Tie Game!')
            tie += 1
            display_options(tie, win, lose)
        elif cpu_selected == 'Paper':
            print("The CPU selected Paper! You Lose!")
            lose += 1
            display_options(tie, win, lose)
        else:
            print("The CPU selected Scissors! You Win!")
            win += 1
            display_options(tie, win, lose)
    elif answer == 'Paper':
        if cpu_selected == 'Rock':
            print('The CPU selected Rock! You Win!')
            win += 1
            display_options(tie, win, lose)
        elif cpu_selected == 'Paper':
            print("The CPU selected Paper! Tie Game!")
            tie += 1
            display_options(tie, win, lose)
        else:
            print("The CPU selected Scissors! You Lose!")
            lose += 1
            display_options(tie, win, lose)
    else:
        if cpu_selected == 'Rock':
            print('The CPU selected Rock! You Lose!')
            lose += 1
            display_options(tie, win, lose)
        elif cpu_selected == 'Paper':
            print("The CPU selected Paper! You Win!")
            win += 1
            display_options(tie, win, lose)
        else:
            print("The CPU selected Scissors! Tie Game!")
            tie += 1
            display_options(tie, win, lose)

play_game(tie, win, lose)
