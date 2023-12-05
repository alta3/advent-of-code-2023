import re

def calculate_missing_part_sum(engine_schematic_file):
    # Read the engine schematic from the specified file
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

    # Calculate and return the sum of all part number's value
    total_sum = sum(sum(part) for part in part_numbers.values())
    return total_sum

# Provide the path to the engine schematic file
engine_schematic_file_path = 'gear_data.txt'

# Call the function to calculate the missing part sum and print the result
missing_part_sum = calculate_missing_part_sum(engine_schematic_file_path)
print(f"The sum of all part numbers in the engine schematic is: {missing_part_sum}")
