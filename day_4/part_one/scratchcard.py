# Python script to process scratchcards data

# Define a function to process each line of the scratchcards data
def process_line(line):
    # Split the line into two sides using the '|' character
    left_side, right_side = line.split('|')
    
    # Create sets of numbers from the left and right sides, stripping extra whitespaces
    left_numbers = set(left_side.strip().split())
    right_numbers = set(right_side.strip().split())
    
    # Find the intersection (common elements) between the two sets
    matches = left_numbers.intersection(right_numbers)
    
    # Calculate the value for the line based on the number of matches
    if len(matches) > 0:
        # Use the formula 2^(n-1) to calculate the value, where n is the number of matches
        return 2 ** (len(matches) - 1)
    else:
        # If there are no matches, the line is worth 0 points
        return 0

# Define the main function
def main():
    # Initialize a variable to store the total sum of points
    total_sum = 0
    
    # Open the file 'scratchcards_data.txt' in read mode
    with open('scratchcards_data.txt', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Add the points calculated for each line to the total sum
            total_sum += process_line(line)
    
    # Print the total sum of points
    print(f"The total sum is: {total_sum}")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function
    main()
