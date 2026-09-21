import random

def get_win(computer , user):
    if user == computer:
        return None

    # Snake vs Water
    if user == "s" and computer == "w":
        return True
    if user == "w" and computer == "s":
        return False
    
    # Snake vs Gun
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False
    
    # Gun vs Water
    if user == "g" and computer == "w":
        return False
    if user == "w" and computer == "g":
        return True


random_no = random.randint(1,3)
print("Computer Turn : Snake(s),  Water(w), Gun(g)")

if(random_no == 1):
    computer = "s"
elif(random_no == 2):
    computer = "w"
else:
    computer = "g"

user = input("Your Turn : Snake(s), Water(w) , Gun(g) : ").lower()
result = get_win (computer , user)
print("Computer Turn : ",computer)
print("User Turn : ",user)

if result is None:
    print("Match Draw!")
elif result == True:
    print("You Win!")
else:
    print("You lose!")