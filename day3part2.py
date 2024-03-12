def calculate_sum_around_star(engine_schematic):
    rows = len(engine_schematic)
    cols = len(engine_schematic[0])

    total_sum = 0

    for row in range(rows):
        for col in range(cols):
            if engine_schematic[row][col] == '*':
                list_nums_around_star = []

                for i in range(row - 1, row + 2):
                    things_visited = set()
                    for j in range(col - 1, col + 2):
                        if 0 <= i < rows and 0 <= j < cols and j not in things_visited:
                            if engine_schematic[i][j].isdigit():
                                current_num = ""
                                furthest_back = j

                                # Move backward
                                while furthest_back >= 0 and engine_schematic[i][furthest_back].isdigit():
                                    furthest_back -= 1
                                furthest_back += 1
                                # Move forward
                                while furthest_back < cols and engine_schematic[i][furthest_back].isdigit():
                                    current_num += engine_schematic[i][furthest_back]
                                    things_visited.add(furthest_back)
                                    furthest_back += 1

                                if current_num:
                                    list_nums_around_star.append(int(current_num))
                                    current_num = ""

                if len(list_nums_around_star) == 2:
                    print(list_nums_around_star)
                    total_sum += list_nums_around_star[0] * list_nums_around_star[1]
    return total_sum

# File path to read engine schematic from
file_path = r"C:\Users\Rio\OneDrive\Documents\Python happies\AdventOfCode2023\day3input.txt"

# Read engine schematic from file
with open(file_path, 'r') as file:
    engine_schematic = [line.strip() for line in file]

# Calculate the sum based on the described logic
result_sum = calculate_sum_around_star(engine_schematic)

# Print the result
print(f"The sum of products around '*' in the engine schematic is: {result_sum}")

#split the input into a list of lists
#make a variable sum = 0
#loop through each line
#for each line, loop through the chars in the line
#if the char is a *, make an empty list of strings listNumsAround* = [], an empty set thingsVisited, and an integer yAt
#then look at the 3x3 around the * and check if that y position is the same as yAt. if it is, check if the x is in thingsVisited
#otherwise clear thingsVisited and continues looking at the 3x3
#if any of them are digits, make a string currentNum = "" and integer furthestBack equal to the current position in the line
#and make a set that contains the x position of the integers visited
#then start a while loop that goes backwards until it reaches a non-digit and keep updating furthestBack to the current position
#when it reaches a non-digit, it goes to another while loop going forward for as long as it's a digit and adding to currentNum
#once that while loop finishes we add currentNum to listNumsAround and set currentNum back to ""
#then once we've gone through all the surrounding ones we check if listNumsAround.length == 2, and if it does we add their product to sum
