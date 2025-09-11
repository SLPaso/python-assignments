import re

# I. Extract email addresses
def extract_emails(text):
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    return emails

# II. Validate date format (YYYY-MM-DD)
def validate_date(date_string):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date_string))

# III. Replace word in a string
def replace_word(text, old_word, new_word):
    return re.sub(rf'\b{old_word}\b', new_word, text)

# IV. Split string by non-alphanumeric characters
def split_string(text):
    return re.split(r'\W+', text)

# Example usage
text = "Contact us at email@example.com and admin@domain.org. Date: 2023-05-01."
print("Extracted emails:", extract_emails(text))
print("Is valid date:", validate_date("2023-05-01"))
print("Replaced text:", replace_word("Hello world!", "world", "Python"))
print("Split string:", split_string("Hello, world! How are you?"))