# Define a function to find possible games based on the given cube configuration
def possible_games(cubes):
    # List to store IDs of possible games
    possible = []

    # Open the file containing game data
    with open('Cube_Data.txt', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into game ID and cubes information
            game_id, cubes_str = line.split(':')
            cubes_list = cubes_str.strip().split(';')

            # Flag to check if the game is valid
            valid = True

            # Iterate through subsets of cubes in each game
            for subset in cubes_list:
                # Split the subset into individual colors and their counts
                colors = subset.split(', ')
                count = 0

                # Iterate through each color in the subset
                for color in colors:
                    # Extract the count and color name
                    num = int(color.split()[0])

                    # Check if the count exceeds the available cubes for that color
                    if color.endswith('red') and num > cubes['red']:
                        valid = False
                        break
                    elif color.endswith('green') and num > cubes['green']:
                        valid = False
                        break
                    elif color.endswith('blue') and num > cubes['blue']:
                        valid = False
                        break
                    else:
                        count += num

            # If the game is valid, add its ID to the possible list
            if valid:
                possible.append(int(game_id.split()[1]))

    # Return the list of possible game IDs
    return possible

# Define the cube configuration
cubes = {'red': 12, 'green': 13, 'blue': 14}

# Find possible games based on the cube configuration
possible = possible_games(cubes)

# Calculate the sum of IDs of possible games
sum_ids = sum(possible)

# Print the results
print(f"The possible games are: {possible}")
print(f"The sum of the IDs of the possible games is: {sum_ids}")


# Answer is 2771