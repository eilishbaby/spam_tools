def collect_emails(num_emails):
    email_contents = []
    for i in range(num_emails):
        file_path = input(f"Enter the file path for email {i + 1}: ")
        try:
            with open(file_path, 'r') as file:
                email_contents.append(file.read())
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
    return email_contents

def append_to_file(file_path, email_contents):
    try:
        with open(file_path, 'a') as file:
            for content in email_contents:
                file.write(content)
                file.write('\n---\n')  # Separator between emails
        print(f"Emails successfully appended to {file_path}")
    except IOError:
        print(f"An error occurred while appending emails to {file_path}")

def main():
    num_emails = 5
    file_path = "stream_mail.txt"
    email_contents = collect_emails(num_emails)
    if email_contents:
        append_to_file(file_path, email_contents)

if __name__ == '__main__':
    main()
