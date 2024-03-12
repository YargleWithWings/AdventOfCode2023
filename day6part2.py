file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day6input.txt"

with open(file_path, 'r') as file:
   times = file.readline().split(":")[1].split()
   recordDistances = file.readline().split(":")[1].split()

time = ""
for t in times:
   time += t

recordDistance = ""
for d in recordDistances:
   recordDistance += d

totalTimes = 0
time = int(time)
recordDistance = int(recordDistance)
for j in range(1,time):
   if j*(time-j) > recordDistance:
      totalTimes += 1

print(totalTimes)

