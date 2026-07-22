text = "Kavya bought a laptop. she uses it for programming."
references = {
    "She": "Kavya",
    "it": "laptop"
}
print("Text:")
print(text)
print("\nResolved References:")
for pronoun, reference in references.items():
    print(pronoun, "->",reference)