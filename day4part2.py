import time
file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day4input.txt"

time1 = time.time()

dictionary = {"Card " + str(i): 1 for i in range(1, 202)}

with open(file_path, 'r') as file:
   for line in file:
      temp, data = line.split(":")
      discard, cardNum = temp.split()
      discard, num = temp.split()
      num.strip()
      winningCards, myCards = data.split("|")
      listWinningCards = winningCards.split()
      listMyCards = myCards.split()

      numSuccesses = 0
      for winningCard in listWinningCards:
         if winningCard in listMyCards:
            numSuccesses += 1
            #print("Card ", temp)
            dictionary["Card " + str(int(cardNum) + numSuccesses)] += dictionary["Card " + num]

totalCards = 0
for value in dictionary.values():
   totalCards += value

#print(totalCards)

time2 = time.time()

def get_wins():
    acc = 0
    with open(file_path, "r") as file: 
        lines = file.readlines()
        for line in lines:
            a = 1
            wins = card_wins(line)
            #print(wins)
            for i in range(wins - 1):
                    a = a * 2
            #print(a)
            if wins > 0:
                 acc += a
    print(acc)

def card_wins(line):
    matches = 0
    rows = line.split("|")
    rows[0] = rows[0].split(":")[1].split()
    rows[1] = rows[1].strip().split()
    for i in range(len(rows[0])):
        if rows[0][i] in rows[1]:
             matches += 1
    #print(matches)
    return matches

def get_scratchcards():
    acc = 0
    wins_per_card = {}
    card_amt = {}
    with open(file_path, "r") as file: 
        lines = file.readlines()
        for line in lines:
            a = 1
            wins = card_wins(line)
            wins_per_card[lines.index(line)] = wins
    card_amt = wins_per_card.copy()
    for card in card_amt: 
        card_amt[card] = 1
    for card in wins_per_card:
        for j in range(card_amt[card]):
            for i in range(wins_per_card[card]):
                card_amt[card + i + 1] += 1        
    for card in card_amt:
        acc += card_amt[card]
    #print(acc)
get_scratchcards()

time3 = time.time()

with open(file_path, 'r') as file:
    cards = file.read()

cards = cards.split('\n')
card_array = [1] * (len(cards))

for i in range(len(cards)):
    card = cards[i][cards[i].index(":") +1:]
    winning, hand = card.split('|')
    winning_array = ' '.join(winning.split()).split(" ")
    hand_array = ' '.join(hand.split()).split(" ")
    counter = 0
    for num in hand_array:
        if num in winning_array:
            counter += 1
    for consecutive in range(1, counter + 1):
        card_array[i + consecutive] = card_array[i + consecutive] + (card_array[i])
time4 = time.time()

elapsed_time_jacob = (time3 - time2)
elapsed_time_mine = (time2 - time1)
elapsed_time_shreyas = (time4 - time3)

print(f"My function took {elapsed_time_mine} seconds to run, jacob's took {elapsed_time_jacob}, shreyas' took {elapsed_time_shreyas}")

