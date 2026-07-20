import re

products = [
    "Laptop",
    "Laptop Bag",
    "Wireless Mouse",
    "Bluetooth Speaker",
    "Python Book",
    "Java Programming",
    "SQL Guide",
    "Machine Learning Kit"
]

keyword = input("Enter Search Keyword: ")

# Exact Search
exact = [p for p in products if re.fullmatch(keyword, p, re.IGNORECASE)]

# Prefix Search
prefix = [p for p in products if re.match(keyword, p, re.IGNORECASE)]

# Suffix Search
suffix = [p for p in products if re.search(keyword + r'$', p, re.IGNORECASE)]

# Partial Search
partial = [p for p in products if re.search(keyword, p, re.IGNORECASE)]

print("\nExact Match")
print(exact)

print("\nPrefix Match")
print(prefix)

print("\nSuffix Match")
print(suffix)

print("\nPartial Match")
print(partial)

print("\nSearch Report")
print("Exact Matches :", len(exact))
print("Prefix Matches :", len(prefix))
print("Suffix Matches :", len(suffix))
print("Partial Matches :", len(partial))
