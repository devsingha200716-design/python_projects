import random
num = random.randint(1,1000)
tries =0
# print(num)
while True:
    guess = int(input("Please guess your number between 1 to 1000 -: "))
    if guess == num:
        tries +=1
        print(f"You are right, you guessed the number in {tries} tries")
        break
    elif num< guess:
        tries+=1
        print("Go a little lower")
    elif num>guess:
        tries+=1
        print("Go a little higher") 
    else:
        tries  +=1
        print("Sorry, you are wrong")
