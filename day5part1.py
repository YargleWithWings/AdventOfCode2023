def mapSeedToLocation(seed):
   for conversion in map:
      for line in conversion:
         if(seed >= line[1] and seed <= line[1] + line[2] -1):
            seed += line[0] - line[1]
            break
   return seed

file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day5input.txt"

map = []
with open(file_path, 'r') as file:
   fileString = file.readlines()

seeds = [int(i) for i in fileString[0].split(": ")[1].split()]

toAppend = []
i = 3
while i < len(fileString):
   if(fileString[i] == "\n"):
      map.append(toAppend)
      toAppend = []
      i+=1
   else:
      toAppend.append([int(j) for j in fileString[i].strip().split()])
   i+=1
map.append(toAppend)
seedArray = [] 
for seed in seeds:
   seedArray.append(mapSeedToLocation(seed))

seedArray.sort()

print(seedArray[0])

