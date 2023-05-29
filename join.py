def merge_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'a') as output:
        content1 = f1.read()
        content2 = f2.read()

        output.write(content1)
        output.write(content2)

    print(f"Files '{file1}' and '{file2}' merged and appended to '{output_file}'.")


file1 = 'standlist.txt'
file2 = 'wind7.txt'
output_file = 'wind8.txt'

merge_files(file1, file2, output_file)
