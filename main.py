import re

def extract_emails(text):
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/?(?:[\w./?#=&-]*)'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r'(\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4})'
    return re.findall(pattern, text)

def extract_credit_cards(text):
    pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
    return re.findall(pattern, text)

def extract_currency(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)

# Demo run
if __name__ == "__main__":
    with open('test_data.txt', 'r') as file:
        data = file.read()

    print("📧 Emails:", extract_emails(data))
    print("🔗 URLs:", extract_urls(data))
    print("📞 Phone Numbers:", extract_phone_numbers(data))
    print("💳 Credit Cards:", extract_credit_cards(data))
    print("💰 Currency:", extract_currency(data))
