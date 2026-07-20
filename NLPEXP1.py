import re

text = "My email is kavya@gmail.com"

# Search
result = re.search("gmail", text)

if result:
    print("Pattern Found")
else:
    print("Pattern Not Found")

# Match
match = re.match("My", text)

if match:
    print("Text starts with 'My'")
else:
    print("No Match")
