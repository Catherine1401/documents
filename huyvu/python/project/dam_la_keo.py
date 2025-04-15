from random import randint
computer = randint(0,2)

if computer == 0:
    computer = "đấm"
elif computer == 1:
    computer = "lá" 
else:
    computer = "kéo" 


print("Hãy nhập kéo, búa, lá: ")
player = input()

print("Bạn chọn: " + player)
print("Máy chọn: " + computer)
if player == computer:
    print("draw")
else:
    if player == "đấm":
        if computer == "lá":
            print("lose")
        else:
            print("win")
    elif player == "lá":
        if computer == "đấm":
            print("win")
        else:
            print("lose")
    elif player == "kéo":
        if computer == "lá":
            print("win")
        else:
            print("lose")
    else:
        print("Vui lòng nhập lại")