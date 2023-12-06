def is_adjacent_to_symbol(schematic, row, col):
    symbols = {'*', '#', '+', '$', '%', '/', '=', '@', '-' }
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc
            if 0 <= r < len(schematic) and 0 <= c < len(schematic[0]):
                if schematic[r][c] in symbols:
                    return True
    return False

def sum_part_numbers(schematic):
    total_sum = 0
    for row in range(len(schematic)):
        for col in range(len(schematic[0])):
            if schematic[row][col].isdigit():
                # Check if the current digit is part of a number
                number_str = schematic[row][col]
                offset = 1
                while col + offset < len(schematic[0]) and schematic[row][col + offset].isdigit():
                    number_str += schematic[row][col + offset]
                    offset += 1
                # Convert to integer and check if it's adjacent to a symbol
                number = int(number_str)
                if is_adjacent_to_symbol(schematic, row, col):
                    total_sum += number
                # Skip the rest of the digits in the number
                col += offset - 1
    return total_sum

# Load the schematic from 'gear_data.txt'
with open('gear_data.txt', 'r') as file:
    schematic = file.read().splitlines()

print(f"The sum of all part numbers in the engine schematic is: {sum_part_numbers(schematic)}")
