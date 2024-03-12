def findBoatDistance(numSecondsHeldDown, time):
   return numSecondsHeldDown*time

file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day6inputtest.txt"

with open(file_path, 'r') as file:
   times = file.readline().split(":")[1].split()
   recordDistances = file.readline().split(":")[1].split()

numWaysToBeatRecord = []

for i in range(len(times)):
   totalTimes = 0
   time = int(times[i])
   recordDistance = int(recordDistances[i])
   for j in range(1,time):
      if findBoatDistance(j, time-j) > recordDistance:
         totalTimes += 1
   numWaysToBeatRecord.append(totalTimes)
total = 1
for num in numWaysToBeatRecord:
   print(num)
   total *= num

print(total)
