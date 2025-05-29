print("Welcome to treasure island.\nYour mission is to find the treasure.\n")

side = input("You're at a crossroad? .Choose a side left or right: \n").lower()

if side == "left":
    move = input("You've reached an island. Swim to shore or wait for a boat? swim or wait\n").lower()
    if move == "wait":
        door = input ("A house with 3 doors: red, yellow or blue\n").lower()
        if door == "yellow":
            print("You win..")
        else:
            print("Game over! ")
    else:
        print("Game over! ")
else:
    print("YOu fell into a pit. Game over! ")