from collections import defaultdict
import time
import re

file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day2input.txt"

# Measure the start time
start_time = time.time()
for i in range(1000):
   with open(file_path, 'r') as file:
      total_sum = 0
      for line in file:
         color_dict_mins = defaultdict(int)
         id_section, data = line.split(":")
         _, id_value = id_section.split()
         games = data.split(";")
         for game in games:
               colors = game.split(",")
               for color in colors:
                  amount, color = color.split()
                  color_dict_mins[color] = max(color_dict_mins[color], int(amount))
         total_sum += color_dict_mins["red"] * color_dict_mins["blue"] * color_dict_mins["green"]
      #print(total_sum)

# Measure the middle time
middle_time1 = time.time()

for i in range(1000):
   with open(file_path, 'r') as file:
      sum = 0
      for line in file:
         colorDictMins = {"red":0, "blue":0, "green":0}
         idSection, data = line.split(":")
         discard, id = idSection.split()
         games = data.split(";")
         for game in games:
            colors = game.split(",")
            for color in colors:
               amount, color = color.split()
               if int(amount) > colorDictMins[color]:
                  colorDictMins[color] = int(amount)
         sum += colorDictMins["red"]*colorDictMins["blue"]*colorDictMins["green"]
      #print(sum)

middle_time2 = time.time()

for i in range (1000):
   sumPowers = 0
   with open(file_path, "r") as myFile:
      for line in myFile:
         redList = [int(x) for x in re.findall("\d+(?=\sred)", line)] x
         greenList = [int(x) for x in re.findall("\d+(?=\sgreen)", line)] 
         blueList = [int(x) for x in re.findall("\d+(?=\sblue)", line)] 
         sumPowers+=max(redList) * max(blueList) * max(greenList)

# Measure the end time
end_time = time.time()

elapsed_time_mine = (middle_time2 - middle_time1)*100
elapsed_time_gpt = (middle_time1 - start_time)*100
elapsed_time_saffron = (end_time - middle_time2)

print(f"My function took {elapsed_time_mine} seconds to run, gpt took {elapsed_time_gpt}, saffron took {elapsed_time_saffron}")