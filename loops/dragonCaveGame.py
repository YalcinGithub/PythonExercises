import random
import time

totalGolds = 0


def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


def checkCave(chosenCave, flags, totalGolds):
    print('You approach the cave...')
    #time.sleep(2)
    print('It is dark and spooky...')
    #time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
   # time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        totalGolds += random.randint(1, 20)

        print('Gives you his treasure! You earned ' + str(totalGolds))
    else:
        print('Gobbles you down in one bite!')

        flags = False
        return flags, totalGolds


playAgain = 'yes'
i = 0
flag = True

while flag:
    displayIntro()
    caveNumber = chooseCave()

    print('You approach the cave...')
    # time.sleep(2)
    print('It is dark and spooky...')
    # time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    # time.sleep(2)

    friendlyCave = 1
    #print(friendlyCave)
    if caveNumber == str(friendlyCave):
        golds = random.randint(1, 20)

        print('Gives you his treasure! You earned ' + str(golds))
        totalGolds+=golds
        print("Now you have total of "+str(totalGolds))
    else:
        print('Gobbles you down in one bite!')

        flag = False

