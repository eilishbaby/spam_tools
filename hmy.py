def remove_duplicates(file_name):
    with open(file_name, 'r') as file:
        emails = file.read().splitlines()

    unique_emails = list(set(emails))

    with open('cleaner.txt', 'a') as output_file:
        for email in unique_emails:
            output_file.write(email + '\n')

    print("Duplicate removal complete. Clean emails appended to clean.txt")


# Accept the file name from the user
file_name = input("Enter the name of the file: ")

remove_duplicates(file_name)
