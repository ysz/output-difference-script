import os


def read_file_line_by_line(file_name):
    """
    Generator function to read a file line by line.

    Args:
        file_name (str): Path to the file.

    Yields:
        str: The next line from the file.

    Note:
        Using a generator allows processing of potentially huge files without loading the entire file into memory.
    """
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()


def compare_files(file1, file2, output1, output2):
    """
    Compare two files and output unique lines.

    Args:
        file1 (str): Path to the first input file.
        file2 (str): Path to the second input file.
        output1 (str): Path to save lines unique to file1.
        output2 (str): Path to save lines unique to file2.
    """
    # Ensure the provided files are different
    if os.path.abspath(file1) == os.path.abspath(file2):
        raise ValueError("The two input paths point to the same file. Please provide two distinct files.")

    # Create generators to read lines from both files
    generator1 = read_file_line_by_line(file1)
    generator2 = read_file_line_by_line(file2)

    # Initial lines from both files
    line1 = next(generator1, None)
    line2 = next(generator2, None)

    # Lists to hold unique lines from both files
    unique_to_file1 = []
    unique_to_file2 = []

    prev_line1 = None
    prev_line2 = None

    # Loop until lines from both files are exhausted
    while line1 is not None or line2 is not None:
        # Ensure lexicographical ordering within each file
        if prev_line1 and line1 and line1 < prev_line1:
            raise ValueError(f"{file1} is not lexicographically sorted.")
        if prev_line2 and line2 and line2 < prev_line2:
            raise ValueError(f"{file2} is not lexicographically sorted.")

        # Logic to determine unique lines and move to next lines
        if line2 is None or (line1 is not None and line1 < line2):
            unique_to_file1.append(line1)
            prev_line1 = line1
            line1 = next(generator1, None)
        elif line1 is None or (line2 is not None and line1 > line2):
            unique_to_file2.append(line2)
            prev_line2 = line2
            line2 = next(generator2, None)
        else:
            prev_line1 = line1
            prev_line2 = line2
            line1 = next(generator1, None)
            line2 = next(generator2, None)

    # Create "Output" directory if it doesn't exist
    if not os.path.exists("Output"):
        os.makedirs("Output")

    # Save unique lines to respective output files
    with open(os.path.join("Output", output1), 'w') as out1, open(os.path.join("Output", output2), 'w') as out2:
        out1.write('\n'.join(unique_to_file1))
        out2.write('\n'.join(unique_to_file2))


def get_validated_filepath(prompt_message):
    """
    Prompt the user for a file path and validate its existence.

    Args:
        prompt_message (str): Message to display to the user.

    Returns:
        str: Absolute path of the validated file.
    """
    file_path = input(prompt_message).strip().replace('\\', '')
    absolute_path = os.path.abspath(file_path)

    # Check if the provided file path exists
    if not os.path.exists(absolute_path):
        raise ValueError(f"File '{file_path}' not found. Resolved Absolute Path: '{absolute_path}'")

    return absolute_path


if __name__ == "__main__":
    try:
        # Prompt user for input file paths and validate them
        input_file1 = get_validated_filepath("Please enter the path for input file 1: ")
        input_file2 = get_validated_filepath("Please enter the path for input file 2: ")

        # Compare the files and generate output
        compare_files(input_file1, input_file2, 'output1.txt', 'output2.txt')
        print("Processing complete!")
        print("Unique entries have been saved in the 'Output' directory.")

    except Exception as e:
        # Handle any errors that might occur during execution
        print(f"Error: {e}")


