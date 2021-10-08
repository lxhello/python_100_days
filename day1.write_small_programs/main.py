'''
find out the number of all daffodils

for num in range(100, 999):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

'''
import random
import time

'''
hundred money and chickens

for cock in range(0, 20):
    for hen in range(0, 33):
        chick = 100 - cock - hen
        if cock * 5 + hen * 3 + chick / 3 == 100:
            print("cock is {},hen is {},chick is {}".format(cock, hen, chick))
'''

'''
gambling games
'''

total_golds = 1000
while total_golds > 0:
    print("your golds is:", total_golds)
    needs_go_on = False
    while True:
        bet_amount = int(input("please enter bet amount:"))
        if bet_amount > total_golds or bet_amount < 0:
            print("you do not have that much money")
        else:
            break
    first_point = random.randint(1, 7) + random.randint(1, 7)
    print("current points is",first_point)
    if first_point == 7 or first_point == 11:
        print("player win")
        total_golds += bet_amount
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print("master win")
        total_golds -= bet_amount
    else:
        needs_go_on = True
        print("you need roll the dice again")
        time.sleep(5)
    while needs_go_on:
        needs_go_on = False
        second_point = random.randint(1, 7) + random.randint(1, 7)
        print("current points is",second_point)
        if second_point == 7:
            print("master win")
            total_golds -= bet_amount
        elif second_point == first_point:
            print("player win")
            total_golds += bet_amount
        else:
            needs_go_on = True
            print("you need roll the dice again")
            time.sleep(5)
print("you are break,Please come back next time")