#character stats generator 
import os 
import time 
import random 
def Rolldice(sides):
   result =  random.randint(1,sides)
   return result 


def roll_6_and_roll_12():
    roll_6_dice = Rolldice(6)
    roll_12_dice = Rolldice(12)
    health = roll_6_dice * roll_12_dice + (10 / 2)
    return health 

def roll612():
    roll6 = Rolldice(6)
    roll12 = Rolldice(12)
    strength = roll6 * roll12 + (12 / 2 )
    return strength 

print("character generator")
anothercharacter = 'yes'
 
while anothercharacter == 'yes':
    characterfirst = input("What whould you like your chracter's first name to be?>")
    chractersecond = input("What whould you like your chracter's second name to be?>")
    health = str(roll_6_and_roll_12())
    strength = str(roll612())
    time.sleep(3)
    os.system("cls")
    print("Your chracter's name is", characterfirst, chractersecond)
    time.sleep(3)
    print("Your character's health is", health, "hp")
    print("Your character's strength is", strength,"st")
    anothercharacter = input("Whould you like to create another character?>")





