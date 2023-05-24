def remove_valid_word(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    modified_lines = [line.replace('valid', '') for line in lines]

    with open(output_file, 'a') as file:
        for line in modified_lines:
            file.write(line)

    print(f"Lines with 'valid' removed appended to '{output_file}'.")


input_file = input("Enter the input file name: ")
output_file = "overvalid.txt"

remove_valid_word(input_file, output_file)
