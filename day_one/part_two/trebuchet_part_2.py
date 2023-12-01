# Function to convert a line into a two-digit number
def convert_to_two_digit_number(line):
    # Modified word-to-digit mapping to replace words with numerical values-> The numbers are surrounded by their first and last letter because 
    # some of the input strings do things like eighthree, which our code would cover to 8hree but is really 8 and 3.
    word_to_digit = {'one': 'o1e', 'two': 't2e', 'three': 't3e', 'four': 'f4r',
                    'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

    # Iterate over the word-to-digit mapping and replace words with their modified representations
    for word, digit in word_to_digit.items():
        line = line.replace(word, digit)

    # Extract digits from the modified line
    numbers = [char for char in line if char.isdigit()]

    # Check if any numbers were found
    if numbers:
        # Take the first and last digits to form a two-digit number
        first_digit = numbers[0]
        last_digit = numbers[-1]
        two_digit_number = int(f"{first_digit}{last_digit}")
        return two_digit_number
    else:
        # If no numbers found in the line, return None or handle it as needed
        return None

# Function to process a text file and calculate the sum of two-digit numbers
def process_txt_file(file_path):
    # Initialize an empty list to store two-digit numbers
    two_digit_numbers = []
    try:
        # Open the specified text file for reading
        with open(file_path, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Convert the line to a two-digit number using the modified function
                two_digit_number = convert_to_two_digit_number(line)
                
                # Check if a valid two-digit number was obtained
                if two_digit_number is not None:
                    # Append the two-digit number to the list
                    two_digit_numbers.append(two_digit_number)
            
            # Call the sumTwoDigitNumber function to calculate and print the sum
            sumTwoDigitNumber(two_digit_numbers)
    
    except FileNotFoundError:
        # Handle the case where the specified file is not found
        print(f"File not found: {file_path}")
    except Exception as e:
        # Handle other potential errors during file processing
        print(f"An error occurred: {e}")

# Function to calculate and print the sum of a list of two-digit numbers
def sumTwoDigitNumber(two_digit_numbers):
    # Calculate the sum of two-digit numbers using the sum() function
    total_sum = sum(two_digit_numbers)
    # Print the calculated sum
    print(total_sum)

# Example usage:
# Specify the path to the text file containing the data
txt_file_path = '../part_one/trebuchet_data.txt'
# Call the process_txt_file function to perform the required operations
process_txt_file(txt_file_path)

# Solution: 54649
