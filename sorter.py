def remove_invalid_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    valid_lines = [line.strip() for line in lines if 'invalid' not in line.lower()]

    with open(output_file, 'a') as file:
        for line in valid_lines:
            file.write(line + '\n')

    print(f"Valid lines appended to '{output_file}'.")


input_file = input("Enter the input file name: ")
output_file = "valid.txt"

remove_invalid_lines(input_file, output_file)
