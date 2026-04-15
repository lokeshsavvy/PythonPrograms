import random
Secret_num = random.randint(1,100)
guess_num = 0
print(f"Secret number generated is: {Secret_num}") 
while guess_num != Secret_num:
    guess_num = int(input("Enter the Number: "))
    if guess_num>Secret_num:
        print("guess is too high")
    elif guess_num<Secret_num:
        print("guess is too low")
print("guess is correct")
        





