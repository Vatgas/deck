import random
import numpy as np
import csv

#n = input("Type a value for n: ")
n = 7
nint = 2*int(n)

def generateDeck():#what it says on the tin
    deck = []
    r = 0
    b = 0
    while len(deck) != nint:
        if random.randint(0,1) and r != nint/2:
            deck.append("R")
            r += 1
        elif b != nint/2:
            deck.append("B")
            b += 1
    return deck
def createLoopDeckWithRStart(): #these two methods generate the result we want at the end of the random process
    loop_deck_r = []
    count = 0
    while count != nint:
        if count%2 == 0:
            loop_deck_r.append("R")
            count += 1
        else:
            loop_deck_r.append("B")
            count += 1
    return loop_deck_r
def createLoopDeckWithBStart():
    loop_deck_b = []
    count = 0
    while count != nint:
        if count%2 == 0:
            loop_deck_b.append("B")
            count += 1
        else:
            loop_deck_b.append("R")
            count += 1
    return loop_deck_b
def shuffleDeck(deck = []):
    if deck[0] == deck[nint-1]:
        put_back = deck.pop(0)
        deck.append(put_back)
    else:
        put_back = deck.pop(0)
        deck.insert(random.randint(1,nint - 2), put_back) #don't place the top card at the top or the bottom

# main method
count = 0
trial_time_list = []
loop_deck_r = createLoopDeckWithRStart()
loop_deck_b = createLoopDeckWithBStart()
# limit = input("Enter how many trials you would like to do: ")
while count != 50:
    deck = generateDeck()
    number_of_trials = 0
    # print(deck)
    while deck != loop_deck_r and deck != loop_deck_b:
        shuffleDeck(deck)
    #    print(deck)
        number_of_trials += 1
    # print("The number of trials is: " + str(number_of_trials))
    trial_time_list.append(number_of_trials)
    count += 1
print(trial_time_list)
print(np.mean(trial_time_list))
print(max(trial_time_list))
print(np.std(trial_time_list))
# print("The average number of trials is: " + str(np.mean(trial_time_list)))
# print("The maximum is: ", max(trial_time_list))
# print("The standard deviation is: ", np.std(trial_time_list))
row = [str(n), str(np.mean(trial_time_list)), str(max(trial_time_list)), str(np.std(trial_time_list))]
with open("D:\Documents\python projects\\results.csv", "a") as csvFile:
    writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(row)

csvFile.close()
