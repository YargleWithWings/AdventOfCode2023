file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day1input.txt" #day1input.txt

def findLineTotal(line):
   #find the first integer
   lowestIndex = len(line)
   highestIndex = -1
   firstInt = ""
   lastInt = ""
   for num in spelled_out_numbers:
      firstIndex = line.find(num)
      lastIndex = line.rfind(num)
      if(firstIndex != -1):
         if(firstIndex < lowestIndex):
            lowestIndex = firstIndex
            firstInt = str(spelled_out_numbers.index(num) + 1)
         if(lastIndex > highestIndex):
            highestIndex = lastIndex
            lastInt = str(spelled_out_numbers.index(num) + 1)
   for index2 in range(len(line)):
      char = line[index2]
      if(char.isdigit()):
         if(index2 < lowestIndex):
            lowestIndex = index2
            firstInt = char
         if(index2 > highestIndex):
            highestIndex = index2
            lastInt = char
   return int(firstInt + lastInt)

# Mapping of spelled-out numbers to numeric values
spelled_out_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open(file_path, 'r') as file:
    total = 0
    for line in file:
        total += findLineTotal(line)

print(total)

# Part 2
sum = 0
strToNum = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
strToNumReversed = {}
with open("day1input.txt", "r") as myFile:
    for line in myFile:
        # findall returns capturing groups but matches non-overlapping patterns; this has zero-width matches but returns stuff through the capturing group
        nums = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        sum+= int((nums[0] if len(nums[0]) == 1 else strToNum[nums[0]]) + (nums[-1] if len(nums[-1]) == 1 else strToNum[nums[-1]]))
print(sum)
