# Define a function to calculate the sum of the power of the maximum sets of cubes for each game
def maximum_cubes():
    # Initialize the total power
    total_power = 0

    # Open the file containing game data
    with open('../part_one/Cube_Data.txt', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into game ID and cubes information
            _, cubes_str = line.split(':')
            cubes_list = cubes_str.strip().split(';')

            # Initialize the dictionary to store the maximum number of cubes for each color
            max_cubes = {'red': 0, 'green': 0, 'blue': 0}

            # Iterate through each subset of cubes in the game
            for subset in cubes_list:
                # Split the subset into individual colors and their counts
                colors = subset.split(', ')

                # Iterate through each color in the subset
                for color in colors:
                    # Split the color into count and cube color
                    num_str, cube_color = color.split()
                    num = int(num_str)

                    # Update the maximum number of cubes for each color
                    if num > max_cubes[cube_color]:
                        max_cubes[cube_color] = num

            # Calculate the power of the maximum set and add it to the total power
            power = max_cubes['red'] * max_cubes['green'] * max_cubes['blue']
            total_power += power

    # Return the final sum of powers
    return total_power

# Call the function to get the sum of the power of the maximum sets of cubes
total_power = maximum_cubes()

# Print the result
print(f"The sum of the power of the maximum sets of cubes is: {total_power}")

# The answer is 70924
