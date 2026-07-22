expression = input("Enter expression: ")

predicate = expression.split("(")[0]

arguments = expression.split("(")[1]
arguments = arguments.replace(")", "")
arguments = arguments.split(",")

print("Predicate:", predicate)
print("Arguments:", arguments)