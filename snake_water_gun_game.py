import random

def play_game(no_of_chances):
    width=20
    print("\t\t\t\t\tSnake,Water,Gun Game\n")
    print("'s' for snake, 'w' for water, or 'g' for gun")
    print(f"no of chances limited {no_of_chances} times only")
    chance=1 # Local variable
    computer_point=0 # Local variable
    human_point=0 # Local variable
    while chance<=no_of_chances:
        _input=input("\n'Snake,Water,Gun': ").lower()
        _random=random.choice(["s","w","g"])

        if _input==_random:
            print("Tie 0 to each")
        elif (_input=="s" and _random=="w") or (_input=="w" and _random=="g") or (_input=="g" and _random=="s"):
            human_point+=1
            print(f"you guess {_input} and computer guess is {_random}")
            print("you win 1 point")
            print(f"computer_point is {computer_point} and your point is {human_point}")
        elif (_input=="s" and _random=="g") or (_input=="w" and _random=="s") or (_input=="g" and _random=="w"):
            computer_point+=1
            print(f"you guess {_input} and computer guess is {_random}")
            print("computer win 1 point")
            print(f"computer_point is {computer_point} and your point is {human_point}")
        else:
            print("Unexpected error! invalid input")
        print(no_of_chances-chance,"chances  left  now")
        chance+=1

    if computer_point==human_point:
        print("\nTie")
    elif computer_point>human_point:
        print("\ncomputer win and you loose")
    else:
        print("\nyou win and computer loose")

    print(f"\ncomputer total point is {computer_point} and your total point is {human_point}")
    print("\nTHANKS FOR PLAY")

print("The name is",__name__)
if __name__ == '__main__':
    play_game(9)




# print("eg3rthkyjuk)
