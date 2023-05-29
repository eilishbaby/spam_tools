def extract_email_lines(input_file, output_file, max_lines):
    with open(input_file, 'r') as file:
        email_lines = [line.strip() for line in file if '@' in line]

    num_lines = min(len(email_lines), max_lines)
    selected_lines = email_lines[:num_lines]

    with open(output_file, 'a') as file:
        file.write('\n'.join(selected_lines))

    print(f'{num_lines} lines appended to {output_file}.')


input_filename = 'input.txt'
output_filename = '39.txt'
max_lines = 39000

extract_email_lines(input_filename, output_filename, max_lines)
