file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day4input.txt"

with open(file_path, 'r') as file:
    total = 0
    for line in file:
      temp, data = line.split(":")
      winningCards, myCards = data.split("|")
      listWinningCards = winningCards.split()
      listMyCards = myCards.split()

      cardTotal = 0
      for winningCard in listWinningCards:
         if winningCard in listMyCards:
            if cardTotal == 0:
               cardTotal = 1
            else:
                  cardTotal *= 2
      total += cardTotal
         

print(total)

