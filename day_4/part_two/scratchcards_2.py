# Python script to generate combinations from scratchcards data

# Define a function to generate combinations and count the total number of scratchcards
def generate_combinations(lines):
    # Initialize a list to store the number of combinations for each scratchcard
    card_combinations = [1] * len(lines)
    
    # Iterate through each line of scratchcards data
    for i, line in enumerate(lines):
        # Split the line into two sides using the '|' character
        x, y = map(str.split, line.split('|'))
        
        # Find the number of matches between the two sides
        matches = len(set(x) & set(y))
        
        # Update the combinations for subsequent scratchcards based on matches
        for j in range(i + 1, min(i + 1 + matches, len(lines))):
            card_combinations[j] += card_combinations[i]
    
    # Return the total sum of combinations, which represents the total number of scratchcards
    return sum(card_combinations)

# Example usage
# Open the scratchcards data file and read lines
lines = open('../part_one/scratchcards_data.txt', 'r').readlines()

# Call the generate_combinations function to calculate the total number of scratchcards
total_combinations = generate_combinations(lines)

# Print the total number of scratchcards
print(f"The total number of scratchcards is: {total_combinations}")
