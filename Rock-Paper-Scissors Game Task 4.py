print("**** welcome to rock paper scissor ")

def game():

    while True:

        player=input("\nrock,\npaper,\nscissor :")
        option=["rock","paper","scissor"]

        if player not in option:
            print("invalid input")

            continue

        import random

        computer=["rock","paper","scissors"]
        ran1=random.choice(computer)
        print(f'computer choice is: {ran1}')

        if player==ran1:
            print("draw")

        elif player == 'rock' and ran1 == 'scissors' or \
             player == 'scissors' and ran1 == 'paper' or \
             player == 'paper' and ran1 == 'rock':
            print("player is win")
        
        else:
            print("computer is win ")

        play_again=input("you want play again yes/no :-")
        if play_again!="yes":
            break
        print("*** THANKS FOR PLAYING *****")
game()

 

