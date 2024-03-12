file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day2input.txt"

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
   print(sum)

   