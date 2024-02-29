import re

def lowercase_first_letter(string):
    if string:
        return re.sub(r'^\w', lambda match: match.group(0).lower(), string)
    else:
        return string
