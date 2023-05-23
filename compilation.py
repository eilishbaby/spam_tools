def merge_files(filenames, output_filename):
    with open(output_filename, 'a') as output_file:
        for filename in filenames:
            with open(filename, 'r') as input_file:
                output_file.write(input_file.read())
                output_file.write('\n')  # Add a new line between each file's content

# List to store input filenames
input_files = []

# Accept eight text file paths from the user
for i in range(1, 9):
    file_path = input(f"Enter path of text file {i}: ")
    input_files.append(file_path)

# Output filename
output_file = 'all.txt'

# Merge the files
merge_files(input_files, output_file)

print("Merging completed! The content of all the files has been appended into 'all.txt'.")
