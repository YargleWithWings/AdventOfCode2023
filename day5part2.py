def processRangeSeeds(seeds, ranges, seedMaps):
   newSeeds = []
   newRanges = []
   fragments = seeds
   rangeFragments = ranges
   while (len(fragments) != 0):
      seedBottom = fragments.pop()
      seedRange = rangeFragments.pop()
      seedTop = seedBottom + seedRange
      oldSeedsLength = len(newSeeds)
      for m in range(len(seedMaps)):
         if(oldSeedsLength == len(newSeeds)):
            mapBottom = seedMaps[m][0]
            mapRange = seedMaps[m][1]
            mapTop = mapBottom + mapRange
            dest = seedMaps[m][2]
            
            if (seedBottom < mapBottom and seedTop > mapTop):
                  fragments.append(seedBottom)
                  rangeFragments.append(mapBottom - seedBottom)

                  newSeeds.append(dest)
                  newRanges.append(mapTop - mapBottom)

                  fragments.append(mapTop)
                  rangeFragments.append(seedTop - mapTop)
            elif (seedBottom < mapBottom and seedTop > mapBottom):
                  fragments.append(seedBottom)
                  rangeFragments.append(mapBottom - seedBottom)

                  newSeeds.append(dest)
                  newRanges.append(seedTop - mapBottom)
            elif (seedBottom >= mapBottom and seedBottom < mapTop and seedTop > mapTop):
                  newSeeds.append(seedBottom - mapBottom + dest)
                  newRanges.append(mapTop - seedBottom - 1)

                  fragments.append(mapTop)
                  rangeFragments.append(seedTop - mapTop)
            elif (seedBottom >= mapBottom and seedTop <= mapTop):
                  newSeeds.append(seedBottom - mapBottom + dest)
                  newRanges.append(seedRange)

      if (len(newSeeds) == oldSeedsLength):
         newSeeds.append(seedBottom)
         newRanges.append(seedRange)
   return [newSeeds, newRanges]

def constructMap(arr):
    rangePairs = []
    for n in range(0, len(arr), 3):
        destination = int(arr[n])
        source = int(arr[n + 1])
        range = int(arr[n + 2])
        rangePairs.append([source, range, destination])
    return rangePairs

file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day5inputtest.txt"

maps = []
with open(file_path, 'r') as file:
   fileString = file.readlines()

seeds = [int(i) for i in fileString[0].split(": ")[1].split()]

toAppend = []
i = 3
while i < len(fileString):
   if(fileString[i] == "\n"):
      maps.append(toAppend)
      toAppend = []
      i+=1
   else:
      toAppend.append([int(j) for j in fileString[i].strip().split()])
   i+=1
maps.append(toAppend)

lowest = 1000000000000000000000000
for seedIndex in range(0,len(seeds),2):
   testSeeds = [seeds[seedIndex]]
   ranges = [seeds[seedIndex+1]]
   for individualMap in maps:
      testSeeds, ranges = processRangeSeeds(testSeeds, ranges, individualMap)
   
   for seed in testSeeds:
       if(seed < lowest):
           lowest = seed


print(lowest)

