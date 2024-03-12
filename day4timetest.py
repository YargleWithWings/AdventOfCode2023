import time
import re

file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day4input.txt"

time1 = time.time()

for i in range(1000):
   sum = 0
   with open(file_path) as myFile:
      for line in myFile:
         line = line.split(":")[1]
         winning, have = line.split("|")
         winning = winning.strip().split()
         have = have.strip().split()
         numWinning = 0
         for num in have:
            if num in winning:
               numWinning+=1
         if numWinning > 0:
            sum+=2**(numWinning-1)

time2 = time.time()

for i in range(1000):
   sum = 0
   with open(file_path) as myFile:
      for line in myFile:
         line = line.split(":")[1]
         winning, have = line.split("|")
         winning = re.findall("\d+", winning)
         have = re.findall("\d+", have)
         numWinning = 0
         for num in have:
            if num in winning:
               numWinning+=1
         if numWinning > 0:
            sum+=2**(numWinning-1)

time3 = time.time()

for i in range(1000):
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

time4 = time.time()

elapsed_time_saffron = (time2 - time1)
elapsed_time_regex = (time3 - time2)
elapsed_time_mine = (time4 - time3)

print(f"My function took {elapsed_time_mine} seconds to run, regex took {elapsed_time_regex}, saffron took {elapsed_time_saffron}")