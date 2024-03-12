def is_valid_coordinate(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols

def calculate_sum_of_adjacent_integers(engine_schematic):
    rows = len(engine_schematic)
    cols = len(engine_schematic[0])
    tempNum = ""
    total_sum = 0
    shouldBeCounted = False
    for row in range(rows):
        for col in range(cols):
            if engine_schematic[row][col].isdigit():
               adjacent_coordinates = [
                    (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                    (row, col - 1),                     (row, col + 1),
                    (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
               ]
               if any(is_valid_coordinate(i, j, rows, cols) and (not (engine_schematic[i][j].isdigit() or engine_schematic[i][j] == "."))  for i, j in adjacent_coordinates):
                  shouldBeCounted = True
               tempNum += engine_schematic[row][col]
            elif tempNum:
                if(shouldBeCounted):
                    total_sum += int(tempNum)
                tempNum = ""
                shouldBeCounted = False

    return total_sum

file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day3input.txt"
with open(file_path, 'r') as file:
    engine_schematic = [line.strip() for line in file]

# Calculate the sum of contiguous integers adjacent to symbols in the engine schematic
result_sum = calculate_sum_of_adjacent_integers(engine_schematic)

# Print the result
print(f"The sum of contiguous integers adjacent to symbols in the engine schematic is: {result_sum}")

#split the input into a list of lists
#create a filler variable total and a string thisNum = "" and boolean shouldBeCounted = false
#for loop through each line
#go through each character in the line and ask if it's a digit
#if it's a digit and a thisNum += the current char
#then check every surrounding space to see if it's not a digit and not a period
#if it's not a digit or a period, set shouldBeCounted to true
#once we've checked all the surrounding spaces we move to the next char
#once we hit something that's not a digit we check if "shouldbecounted" is true and if it is we do total += int(thisNum)
#then we set shouldbecounted to false again and thisNum to "" and keep going
