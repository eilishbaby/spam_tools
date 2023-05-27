def collect_unique_emails(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'a') as output:
        emails_file1 = set(f1.read().splitlines())
        emails_file2 = set(f2.read().splitlines())

        unique_emails = emails_file1 - emails_file2

        for email in unique_emails:
            output.write(email + '\n')

    print("Comon complete. Unique emails appended to", output_file)

# Usage example
file1_path = 'all.txt'
file2_path = 'good.txt'
output_file_path = 'unique_emails.txt'

collect_unique_emails(file1_path, file2_path, output_file_path)
