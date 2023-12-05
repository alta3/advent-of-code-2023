import re

def calculate_gear_ratios(engine_schematic_file):
    with open(engine_schematic_file, 'r') as file:
        schematic_lines = [line.strip() for line in file.readlines() if line.strip()]

    
    # Create a dictionary to store part numbers and their neighboring positions
    part_numbers = {}

    # Iterate through each row in the engine schematic, creating a dictionary with keys that have NO values yet. They keys are the row, column where a symbol is found
    for row in range(len(schematic_lines)):
        for col in range(len(schematic_lines[0])):
            # Check if the current character is not a digit or a dot
            current_char = schematic_lines[row][col]
            if current_char not in '01234566789.':
                # If not a digit or dot, add the position to the dictionary with an empty list
                part_numbers[(row, col)] = []
                
    gear_ratios = []

   # Iterate through each row in the engine schematic, ultimately adding the "part number" as a value to the symbol position key it matches.
    for row, line in enumerate(schematic_lines):
        # Use regular expression to find numbers in a string
        for match in re.finditer(r'\d+', line):
            # Identify positions around the numeric value (including diagonals)
            neighbors = {(row, col) for row in (row - 1, row, row + 1)
                           for col in range(match.start() - 1, match.end() + 1)}

            # If a neighbor coordinate is === to a part_number/symbol coordinate, we add the number to the symbol key as a value. 
            for neighbor in neighbors & part_numbers.keys():
                part_numbers[neighbor].append(int(match.group()))

    #Iterate a second time, now looking for * to indicate "gears"
    for row, line in enumerate(schematic_lines):
        for col, char in enumerate(line):
            if char == '*':
                # Check if the '*' has exactly two adjacent part numbers
                adjacent_part_numbers = part_numbers.get((row, col), [])
                if len(adjacent_part_numbers) == 2:
                    # Calculate and store the gear ratio
                    gear_ratio = adjacent_part_numbers[0] * adjacent_part_numbers[1]
                    gear_ratios.append(gear_ratio)

    # Sum up all the gear ratios
    total_gear_ratio = sum(gear_ratios)
    return total_gear_ratio

# Provide the path to the engine schematic file
engine_schematic_file_path = '../part_one/gear_data.txt'

# Call the function to calculate the sum of all gear ratios and print the result
total_gear_ratios = calculate_gear_ratios(engine_schematic_file_path)
print(f"The sum of all gear ratios in the engine schematic is: {total_gear_ratios}")
