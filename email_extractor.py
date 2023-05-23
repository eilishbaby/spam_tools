import re

def extract_emails(input_file):
    with open(input_file, 'r') as file:
        text = file.read()

    # Use regular expression to extract email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(pattern, text)

    return emails

def write_emails(emails):
    with open('arranged.txt', 'w') as file:
        for email in emails:
            file.write(email + '\n')

def main():
    input_file = input("Enter the path to the input file: ")

    emails = extract_emails(input_file)
    write_emails(emails)

    print("Emails extracted and written to arranged.txt.")

if __name__ == '__main__':
    main()
