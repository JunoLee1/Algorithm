import random 
card = [11, 2, 3, 4 ,5 ,6 ,7 ,8, 9, 10, 10, 10, 10]
user =[]
computer = []
for i in range(len(card)):
    checked_card = random.sample(card, 2)
    user.append(checked_card)
    computer.append(checked_card)
    print(user)