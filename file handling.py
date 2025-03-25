def file_processor():
    """Reads a file, modifies its content, and writes to a new file with error handling."""
    try:
        # Get filename from user
        input_filename = input("Enter the input filename: ")
        output_filename = input("Enter the output filename: ")
        
        # Read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (example: convert to uppercase and add line numbers)
        modified_lines = []
        for i, line in enumerate(content.splitlines(), 1):
            modified_lines.append(f"{i}: {line.upper()}")
        modified_content = "\n".join(modified_lines)
        
        # Write to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Success! Modified content written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_filename}' or write to '{output_filename}'.")
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print("Error: Could not decode the file (might be a binary file).")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the program
file_processor()