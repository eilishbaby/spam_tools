def create_text_files(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    file_count = 1
    line_count = 0
    file_lines = []

    for line in lines:
        file_lines.append(line)
        line_count += 1

        if line_count == 100:
            write_to_file(file_lines, file_count)
            file_count += 1
            line_count = 0
            file_lines = []

    # Write any remaining lines to the last file
    if file_lines:
        write_to_file(file_lines, file_count)

def write_to_file(lines, file_count):
    output_file = f"output_{file_count}.txt"
    with open(output_file, 'w') as file:
        file.writelines(lines)

def main():
    input_file = input("Enter the path to the input file: ")
    create_text_files(input_file)
    print("Text files created successfully.")

if __name__ == '__main__':
    main()
