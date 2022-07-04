name = input("Enter your name: ")
print("Welcome to this adventure", name)

answer = input("You are on a dirt road, it as come to an end and you can go left or right.Which way would you like to go? ").lower()

if answer == "left":
    left = input("you come to a river, you can work round it or swim across it. Type w to walk and s to swim: ").lower()

    if left == "w":
        print("You walked for many miles, ran out of water and food and lost the game")
    elif left == "s":
        print("You swan across and were eaten by an alligator.")
    else:
        print("Invalid option. You lose!")

elif answer == "right":
    right = input("You came across a bridge, it looks wobbly. Do you want to work across it or head back(cross/back)?: ")
    if right == "cross":
        cross = input("You crossed the bridge and meet a stranger. Do you want to talk to them?(yes/no: ")

        if cross == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif cross == "no":
            print("You ignore the stranger, they get offended and murder you. You LOSE!")
        else:
            print("Invalid option. You lose!")


    elif right == "back":
        print("You go back to the dirt road and loose")
    else:
        print("Invalid option. You lose!")

else:
    print("Invalid option. You lose!")
print("Tank you for trying", name)