# Function to convert a line into a two-digit number
def convert_to_two_digit_number(line):
    # Extract all digits from the line using list comprehension
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
                # Convert the line to a two-digit number using the defined function
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
    # Initialize a variable to store the sum of two-digit numbers
    total_sum = 0
    # Iterate over each two-digit number in the list
    for number in two_digit_numbers:
        # Add the current two-digit number to the total sum
        total_sum += number
    
    # Print the calculated sum
    print(total_sum)

# Example usage:
# Specify the path to the text file containing the data
txt_file_path = 'trebuchet_data.txt'
# Call the process_txt_file function to perform the required operations
process_txt_file(txt_file_path)

# SOLUTION: 54081
