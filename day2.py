file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day2input.txt"

with open(file_path, 'r') as file:
   idSum = 0
   for line in file:
      idSection, data = line.split(":")
      discard, id = idSection.split()
      games = data.split(";")
      valid = True
      for game in games:
         colors = game.split(",")
         for color in colors:
            amount, color = color.split()
            if((color == "red" and int(amount) > 12) or (color == "blue" and int(amount) > 14) or (color == "green" and int(amount) > 13)):
               valid = False
      if valid:
         idSum += int(id)
   print(idSum)

   