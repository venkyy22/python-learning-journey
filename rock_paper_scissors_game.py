laptop = random.choice([1,-1,0])
youStr = input("enter your choice:")
youDict = {"s": 1 , "w" : -1 , "g" : 0}
reversedDict = {1 : "Rock" , -1 : "Paper" , 0 : "Scissors"}

you = youDict[youStr]

# By now we have two variables , you and the  laptop

print(f"you chose {reversedDict[you]}\ncomputer choose {reversedDict[laptop]}")

if laptop == you :
    print("it is a draw ")

else :
    if laptop == -1 and you == 1 :
        print("you win")

    elif laptop == 1 and you == -1:
        print("you lose")

    elif laptop == -1 and you == 0:
        print("you won ")

    elif laptop == 0 and you == -1:
        print("you lose")

    elif laptop == 1 and you == 0:
        print("you lose")

    elif laptop == 0 and you == 1:
        print("you won ")

    else :
        print("something went wrong")
